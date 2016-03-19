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

        # Reset viewport
        for area in bpy.context.screen.areas:
            if area.type == 'VIEW_3D':
                for space in area.spaces:
                    if space.type == 'VIEW_3D':
                        space.show_only_render = True

                        region = space.region_3d

                        region.view_location.x = 0
                        region.view_location.y = 0
                        region.view_location.z = 0

                        region.view_rotation.w = 1
                        region.view_rotation.x = 0
                        region.view_rotation.y = 0
                        region.view_rotation.z = 0

                        region.view_distance = 10

        return {'FINISHED'}
