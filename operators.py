import bpy
from bpy.types import Operator


class VCMOperator(Operator):
    """Tooltip"""
    bl_idname = "object.visual_code_machine"
    bl_label = "Visual Code Machine"

    def execute(self, context):
        # Remove all objects
        for obj in bpy.data.objects:
            obj.select = True
        bpy.ops.object.delete()

        return {'FINISHED'}
