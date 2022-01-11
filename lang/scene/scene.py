import time, sys, logging, bpy, os
from bpy.types import Scene, Object
from bpy.props import IntVectorProperty
from ...types import BFNamelist, FDSCase, BFException, BFNotImported
from ... import utils
from ..object.MOVE import ON_MOVE

log = logging.getLogger(__name__)


class BFScene:
    """!
    Extension of Blender Scene.
    """

    @property
    def bf_namelists(self):
        """!
        Return related bf_namelist, instance of BFNamelist.
        """
        return (n(self) for n in BFNamelist.subclasses if n.bpy_type == Scene)

    def to_fds(self, context, full=False, all_surfs=False, filepath=None):
        """!
        Return the FDS formatted string.
        @param context: the Blender context.
        @param full: if True, return full FDS case.
        @param all_surfs: if True, return all SURF namelists, even if not related.
        @param filepath: filepath of FDS case to be exported.
        @return FDS formatted string (eg. "&OBST ID='Test' /"), or None.
        """
        lines = list()

        # Set mysef as the right Scene instance in the context
        # FIXME should not be needed, see bpy.context
        bpy.context.window.scene = self

        # Get scene name and dir from filepath
        if not bpy.data.is_saved:
            raise BFException(self, "Save the current Blender file before exporting.")
        self.name, self.bf_config_directory = utils.os_filepath_to_bl(
            bpy.path.abspath(filepath)
        )

        # Header
        if full:
            v = sys.modules["blenderfds"].bl_info["version"]
            blv = bpy.app.version_string
            now = time.strftime("%a, %d %b %Y, %H:%M:%S", time.localtime())
            blend_filepath = bpy.data.filepath or "not saved"
            if len(blend_filepath) > 60:
                blend_filepath = "..." + blend_filepath[-57:]
            lines.extend(  # header has !!!
                (
                    f"!!! Generated by BlenderFDS {v[0]}.{v[1]}.{v[2]} on Blender {blv}",
                    f"!!! Date: <{now}>",
                    f"!!! File: <{blend_filepath}>",
                    f"! --- Case from Blender Scene <{self.name}> and View Layer <{context.view_layer.name}>",
                )
            )

        # Scene namelists
        lines.extend(
            bf_namelist.to_fds(context)
            for bf_namelist in self.bf_namelists
            if bf_namelist
        )

        # Free Text
        if self.bf_config_text:
            text = self.bf_config_text.as_string()
            if text:
                text = f"\n! --- Free text from Blender Text <{self.bf_config_text.name}>\n{text}"
                lines.append(text)

        # Material namelists
        if full:
            if all_surfs:  # all SURFs exported
                mas = list(bpy.data.materials)
                header = "\n! --- Boundary conditions from all Blender Materials"
            else:  # only related SURFs exported
                mas = list(
                    set(
                        ms.material
                        for ob in self.objects
                        for ms in ob.material_slots
                        if ms.material  # not empty
                    )
                )
                header = "\n! --- Boundary conditions from related Blender Materials"
            mas.sort(key=lambda k: k.name)  # alphabetic sorting by name
            ma_lines = list(ma.to_fds(context) for ma in mas)
            if any(ma_lines):
                lines.append(header)
                lines.extend(ma_lines)

        # Objects from collections
        if full:
            lines.append(" ")
            lines.append(self.collection.to_fds(context))

        # TAIL
        if full and self.bf_head_export:
            lines.append("\n&TAIL /\n ")

        # Write to file
        fds_text = "\n".join(l for l in lines if l)
        if filepath:
            utils.write_txt_file(filepath, fds_text)
        else:
            return fds_text

    def from_fds(self, context, filepath=None, f90=None):
        """!
        Set self.bf_namelists from FDSCase, on error raise BFException.
        @param context: the Blender context.
        @param filepath: filepath of FDS case to be imported.
        @param f90: FDS formatted string of namelists, eg. "&OBST ID='Test' /\n&TAIL /".
        """
        # Set mysef as the right Scene instance in the context
        bpy.context.window.scene = self
        # Init
        if filepath and not f90:
            fds_case = FDSCase(filepath=filepath)
            self.bf_config_directory = os.path.dirname(
                filepath
            )  # FIXME set for relative imports of other paths
        elif f90 and not filepath:
            fds_case = FDSCase(f90=f90)
        else:
            raise AssertionError("Either filepath or f90 should be set")
        # Prepare free text for unmanaged namelists
        te = bpy.data.texts.new(f"Imported_text")
        self.bf_config_text = te
        # Import SURFs first to new materials
        while True:
            fds_namelist = fds_case.get_by_label(fds_label="SURF", remove=True)
            if not fds_namelist:
                break
            hid = "Imported_SURF"
            ma = bpy.data.materials.new(hid)
            ma.from_fds(context, fds_namelist=fds_namelist, free_text=te)
            ma.use_fake_user = True  # prevent del (eg. used by PART)
        # Record all MOVEs in a dict
        move_id_to_move = dict()
        while True:
            fds_namelist = fds_case.get_by_label(fds_label="MOVE", remove=True)
            if not fds_namelist:
                break
            # Get ID
            p_id = fds_namelist.get_by_label(fds_label="ID", remove=True)
            if not p_id:
                raise BFNotImported(
                    None, "MOVE namelist requires an ID in <{fds_namelist}>"
                )
            move_id_to_move[p_id.value] = fds_namelist
        # Import OBSTs before VENTs  # TODO generic!
        while True:
            fds_namelist = fds_case.get_by_label(fds_label="OBST", remove=True)
            if not fds_namelist:
                break
            hid = "Imported_OBST"
            me = bpy.data.meshes.new(hid)
            ob = bpy.data.objects.new(hid, object_data=me)
            self.collection.objects.link(ob)
            ob.from_fds(context, fds_namelist=fds_namelist, free_text=te)
        # Then the rest
        fds_case.fds_namelists.reverse()
        while fds_case.fds_namelists:
            fds_namelist = fds_case.fds_namelists.pop()
            imported = False
            # Import to managed BFNamelist
            bf_namelist = BFNamelist.subclasses_by_fds_label.get(
                fds_namelist.fds_label, None
            )
            if bf_namelist:
                hid = f"Imported_{fds_namelist.fds_label}"
                # Into new Object
                if bf_namelist.bpy_type == Object:
                    me = bpy.data.meshes.new(hid)
                    ob = bpy.data.objects.new(hid, object_data=me)
                    self.collection.objects.link(ob)
                    try:
                        ob.from_fds(context, fds_namelist=fds_namelist, free_text=te)
                    except BFNotImported:
                        bpy.data.objects.remove(ob, do_unlink=True)
                    else:
                        imported = True
                # Into current Scene
                elif bf_namelist.bpy_type == Scene:  # in current Scene
                    try:
                        bf_namelist(self).from_fds(
                            context, fds_namelist=fds_namelist, free_text=te
                        )
                    except BFNotImported:
                        pass
                    else:
                        imported = True
                # Unhandled
                else:
                    raise AssertionError(f"Unhandled bf_namelist for <{fds_namelist}>")
            # Import to Free Text
            if not imported:
                te.write(fds_namelist.to_fds(context) + "\n")
        # Transform those Objects that have a MOVE_ID
        for ob in self.collection.objects:
            if ob.bf_move_id_export and ob.bf_move_id:
                try:
                    ON_MOVE(ob).from_fds(
                        context,
                        fds_namelist=move_id_to_move[ob.bf_move_id],
                        free_text=te,
                    )
                except KeyError:
                    raise BFException(
                        self,
                        f"Unknown MOVE namelist <{ob.bf_move_id}> called by Object <{ob.name}>",
                    )
        # Set imported Scene visibility
        context.window.scene = self
        # Show free text
        te.current_line_index = 0
        bpy.ops.scene.bf_show_text()  # FIXME FIXME FIXME remove ops, put py

    @classmethod
    def register(cls):
        """!
        Register related Blender properties.
        @param cls: class to be registered.
        """
        Scene.bf_namelists = cls.bf_namelists
        Scene.to_fds = cls.to_fds
        Scene.from_fds = cls.from_fds
        Scene.bf_file_version = IntVectorProperty(
            name="BlenderFDS File Version", size=3
        )

    @classmethod
    def unregister(cls):
        """!
        Unregister related Blender properties.
        @param cls: class to be unregistered.
        """
        del Scene.bf_file_version
        del Scene.from_fds
        del Scene.to_fds
        del Scene.bf_namelists
