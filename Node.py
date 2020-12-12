__author__ = "Amrutha Varshini Mandalreddy"
__email__ = "am5739@rit.edu"

class attribute:
    def __init__(self, attributeId, attributeName):
        self.attributeId = attributeId
        self.attributeName = attributeName
        self.weight=None

    def updateWeight(self, weight):
        self.weight = weight

    def __str__(self):
        return " Attrubute Id: " + (str)(self.attributeId) + " Attribute Name: " + self.attributeName + " weight " + (str)(self.weight)


class node:
    def __init__(self, data, attribute, depth=1,parent_value=None,  decision = None):
        self.data = data
        self.attribute = attribute
        self.parent_value = parent_value
        self.depth = depth
        self.decision = decision
        self.children = []

    def addChild(self, data, attribute,depth, parent_value, decision=None):
        child = node(data,attribute,depth, parent_value, decision)
        self.children.append(child)
        return child

    def getResult(self, value):
        for child in self.children:
            if child.parent_value == value:
                return child.decision

    def addAttribute(self, attribute):
        self.attribute = attribute

    def getDepth(self):
        return self.depth

    def addDecision(self, result):
        self.decision = result
        #child = node(data,attribute,depth, parent_value, result)
        #self.children.append(child)

    def __str__(self, level=0):
        ret = "\t"*level+str(self.attribute) + " parent Value "+repr(self.parent_value)+ " decision " + repr(self.decision)+ "\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'
        #return f"\n tree( {self.attribute, self.attribute_value, self.decision}): {self.children}"