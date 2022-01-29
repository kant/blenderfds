import logging, re
from bpy.types import Object
from bpy.props import StringProperty
from ...types import BFParam, BFNamelistOb, BFException
from .object import OP_ID, OP_FYI, OP_ID_suffix, OP_other
from .SURF_ID import OP_SURF_ID
from .XB import OP_XB, OP_XB_custom_voxel, OP_XB_voxel_size, OP_XB_center_voxels
from .XYZ import OP_XYZ
from .PB import OP_PB, OP_PBX, OP_PBY, OP_PBZ

log = logging.getLogger(__name__)


class OP_other_namelist(BFParam):
    label = "Label"
    description = "Other namelist label, eg <ABCD>"
    bpy_type = Object
    bpy_prop = StringProperty
    bpy_idname = "bf_other_namelist"
    bpy_default = "ABCD"
    bpy_other = {"maxlen": 4}

    def check(self, context):
        if not re.match("^[A-Z0-9_]{4}$", self.element.bf_other_namelist):
            raise BFException(
                self,
                f"Malformed other namelist label <{self.element.bf_other_namelist}>",
            )


class ON_other(BFNamelistOb):
    label = "Other"
    description = "Other namelist"
    enum_id = 1007
    bf_params = (
        OP_other_namelist,
        OP_ID,
        OP_FYI,
        OP_SURF_ID,
        OP_XB,
        OP_XB_custom_voxel,
        OP_XB_voxel_size,
        OP_XB_center_voxels,
        OP_XYZ,
        OP_PB,
        OP_PBX,
        OP_PBY,
        OP_PBZ,
        OP_ID_suffix,
        OP_other,
    )

    @property
    def fds_label(self):
        return self.element.bf_other_namelist
