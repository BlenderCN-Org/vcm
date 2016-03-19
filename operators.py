import bpy
from bpy.types import Operator


class VCMOperator(Operator):
    """Tooltip"""
    bl_idname = "object.visual_code_machine"
    bl_label = "Visual Code Machine"

    def execute(self, context):
        # Create new screen
        index = bpy.data.screens.values().index(bpy.context.screen)
        bpy.ops.screen.new()
        vcm_screen = bpy.data.screens[index + 1]
        vcm_screen.name = "VCM"

        # Remove all objects
        for obj in bpy.data.objects:
            obj.select = True
        bpy.ops.object.delete()

        # Reset viewport
        for area in vcm_screen.areas:
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
