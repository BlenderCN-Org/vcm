import bpy


class VCMOperator(bpy.types.Operator):
    """Tooltip"""
    bl_idname = "object.visual_code_machine"
    bl_label = "Visual Code Machine"

    def execute(self, context):
        vcm_screen = None

        # Select VCM screen if exists
        for screen in bpy.data.screens:
            if screen.name == "VCM":
                bpy.context.window.screen = screen
                vcm_screen = screen
                break

        # Create new VCM screen if not exists
        if not vcm_screen:
            index = bpy.data.screens.values().index(bpy.context.screen)
            bpy.ops.screen.new()
            vcm_screen = bpy.data.screens[index + 1]
            vcm_screen.name = "VCM"

        # Remove all objects
        for obj in bpy.data.objects:
            obj.select = True
        bpy.ops.object.delete()

        # Remove areas
        while len(vcm_screen.areas) > 1:
            for area1 in vcm_screen.areas:
                for area2 in vcm_screen.areas:
                    if area1 == area2:
                        continue
                    if len(area1.regions) > 1:
                        overdrive = {'window': bpy.context.window, 'screen': vcm_screen, 'area': area1, 'region': area1.regions[1]}
                        result = bpy.ops.screen.area_join(overdrive, min_x=area1.x, min_y=area1.y, max_x=area2.x, max_y=area2.y)
                        if result == {'FINISHED'}:
                            break

        area = vcm_screen.areas[0]
        area.type = 'VIEW_3D'

        # Reset viewport
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
