
import scipy.spatial as graph
import numpy as np

class Node:

# CLASS VAR:  curIndex is used to make sure that all nodes have a unique label.  Incremented every time a new
#  node is generated.
    curIndex=1

    # CLASS METHOD.  Allows for reseting the index counter for generating new nodes. Used only for debugging!
    def reset(cls):
        cls.curIndex=1

    # Create a new node at point x-y.  Optionally pass in a label for the node.  If no explicit label is passed
    # in (which is usually the case), it auto-generates the next label in a sequences starting with A-Z, then
    # going to AA, AB, AC, etc.
    def __init__(self,newX,newY, newLabel= '*'):
        self.x=newX
        self.y=newY
        if newLabel=='*':
            self.label=self.makeLabel()
        else:
            self.label=newLabel

    # Makes an upper case label starting at 'A'.  If >26 nodes, goes to 'AB', 'AC', etc.
    # Works by basically counting in Base26:  converts the index into strings in Base26!
    def makeLabel(self):
        index=self.curIndex
        out = []
        while index>25:
            out.append(index % 26)
            index = int(index / 26)

        out.append(index-1)
        out.reverse()
        node_g.curIndex +=1
        return "".join([chr(65+x) for x in out])


    # Distance:  returns the cartesian distance between this node some other node that is passed in.
    def distance(self,aNode):
        return graph.distance.euclidean([self.x,self.y],[aNode.x,aNode.y])

    def get(self):
        return ([self.x,self.y],self.label)



# Unit tests
# x=Node(4,5)
# y=Node(1,2)
# print(x.get())
# print(y.get())

