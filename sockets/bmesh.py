import bpy
import bmesh
from .. base_types.socket import AnimationNodeSocket

class BMeshSocket(bpy.types.NodeSocket, AnimationNodeSocket):
    bl_idname = "an_BMeshSocket"
    bl_label = "BMesh Socket"
    dataType = "BMesh"
    allowedInputTypes = ["BMesh"]
    drawColor = (0.1, 1.0, 0.1, 1)
    storable = False
    comparable = True

    @classmethod
    def getDefaultValue(cls):
        return bmesh.new()

    @classmethod
    def getCopyExpression(cls):
        return "value.copy()"
