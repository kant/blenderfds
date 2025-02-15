# SPDX-License-Identifier: GPL-3.0-or-later

import logging, os, bpy
from bpy.types import Scene
from bpy.props import (
    BoolProperty,
    FloatProperty,
    StringProperty,
    PointerProperty,
    EnumProperty,
    IntProperty,
)
from ..config import LP
from ..types import BFParam, BFNamelistSc, BFException

log = logging.getLogger(__name__)


class SP_config_case_name(BFParam):
    label = "Filename"
    description = "Filename for exported FDS case,\nalso used as HEAD CHID"
    bpy_type = Scene
    bpy_idname = "name"

    def copy_to(self, context, dest_element):
        pass

    def draw_operators(self, context, layout):
        layout.operator("scene.bf_props_to_scene", icon="COPYDOWN", text="")


class SP_config_directory(BFParam):
    label = "Directory"
    description = "Destination directory for exported FDS case"
    bpy_type = Scene
    bpy_idname = "bf_config_directory"
    bpy_prop = StringProperty
    # no bpy_default, user choice when saving
    bpy_other = {"subtype": "DIR_PATH", "maxlen": 1024}

    def check(self, context):
        if self.get_exported(context):
            value = self.element.bf_config_directory
            if not os.path.exists(bpy.path.abspath(value or "//.")):
                raise BFException(self, f"Case directory <{value}> not existing")

    def copy_to(self, context, dest_element):
        pass


class SP_config_text(BFParam):
    label = "Free Text"
    description = "Internal free text, included verbatim"
    bpy_type = Scene
    bpy_idname = "bf_config_text"
    bpy_prop = PointerProperty
    bpy_other = {"type": bpy.types.Text}

    def draw_operators(self, context, layout):
        layout.operator("scene.bf_show_text", text="", icon="GREASEPENCIL")


class SP_config_text_position(BFParam):
    label = "Free Text Position"
    description = "Set Free Text postion in the exported file"
    bpy_type = Scene
    bpy_idname = "bf_config_text_position"
    bpy_prop = EnumProperty
    bpy_default = "BEGIN"
    bpy_other = {
        "items": (
            (
                "BEGIN",
                "At Beginning",
                "Insert at the beginning of the exported file",
                100,
            ),
            (
                "END",
                "At End",
                "Insert at the end of the exported file",
                500,
            ),
        ),
    }


class SP_config_default_voxel_size(BFParam):
    label = "Default Voxel/Pixel Size"
    description = "Default voxel/pixel resolution"
    bpy_type = Scene
    bpy_idname = "bf_default_voxel_size"
    bpy_prop = FloatProperty
    bpy_default = 0.1
    bpy_other = {
        "step": 1.0,
        "precision": LP,
        "min": 0.001,
        "max": 20.0,
        "unit": "LENGTH",
    }


class SN_config_mpi_processes(BFParam):
    label = "MPI Processes"
    description = (
        "Number of MPI processes automatically allocated to the MESH instances."
    )
    bpy_type = Scene
    bpy_idname = "bf_config_mpi_processes"
    bpy_prop = IntProperty
    bpy_default = 1
    bpy_other = {"min": 1}
    bpy_export = "bf_config_mpi_processes_export"
    bpy_export_default = True


class SN_config_openmp_threads(BFParam):
    label = "OpenMP Threads"
    description = "Number of OpenMP threads assigned to each process."
    bpy_type = Scene
    bpy_idname = "bf_config_openmp_threads"
    bpy_prop = IntProperty
    bpy_default = 1
    bpy_other = {"min": 1}
    bpy_export = "bf_config_openmp_threads_export"
    bpy_export_default = False


class SN_config(BFNamelistSc):
    label = "FDS Case Config"
    bf_params = (
        SP_config_case_name,
        SP_config_directory,
        SP_config_text,
        SP_config_text_position,
        SP_config_default_voxel_size,
        SN_config_mpi_processes,
        SN_config_openmp_threads,
    )

    def draw(self, context, layout):
        row = layout.column(align=True)
        row.operator("scene.bf_show_fds_code", icon="HIDE_OFF")
        return super().draw(context, layout)
