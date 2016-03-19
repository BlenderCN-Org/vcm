bl_info = {
    "name": "Visual Code Machine",
    "description": "IDE for visual programming by Blender",
    "author": "Vladimir Zarypov (krre)",
    "version": (0, 1, 0),
    "blender": (2, 65, 0),
    "location": "Search > Visual Code Machine",
    "warning": "",
    "wiki_url": "http://github.com/krre/vcm",
    "tracker_url": "",
    "support": "COMMUNITY",
    "category": "Development"
}

if "bpy" in locals():
    import imp
    if "operators" in locals():
        imp.reload(operators)

import bpy
from . import operators


def register():
    bpy.utils.register_module(__name__)


def unregister():
    bpy.utils.unregister_module(__name__)

if __name__ == "__main__":
    register()
