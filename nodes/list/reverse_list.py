import bpy
from bpy.props import *
from ... sockets.info import isList
from ... base_types import AnimationNode, UpdateAssignedListDataType

class ReverseListNode(bpy.types.Node, AnimationNode):
    bl_idname = "an_ReverseListNode"
    bl_label = "Reverse List"

    assignedType = StringProperty(update = AnimationNode.updateSockets, default = "Float List")

    def create(self):
        listDataType = self.assignedType
        self.newInput(listDataType, "List", "inList", dataIsModified = True)
        self.newOutput(listDataType, "Reversed List", "reversedList")

        self.newSocketEffect(UpdateAssignedListDataType("assignedType", "LIST",
            [(self.inputs[0], "LIST"),
             (self.outputs[0], "LIST")]
        ))

    def getExecutionCode(self):
        reverseCode = self.inputs[0].getReverseCode().replace("value", "inList")
        return "reversedList = " + reverseCode

    def assignType(self, listDataType):
        if not isList(listDataType): return
        if listDataType == self.assignedType: return
        self.assignedType = listDataType
