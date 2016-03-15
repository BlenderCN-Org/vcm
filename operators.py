import bpy
from bpy.types import Operator

class VCMOperator(Operator):
    """Tooltip"""
    bl_idname = "object.visual_code_machine"
    bl_label = "Visual Code Machine"

    def execute(self, context):
        self.report({'INFO'}, "%i objects selected" % len(context.selected_objects))
        return {'FINISHED'}
