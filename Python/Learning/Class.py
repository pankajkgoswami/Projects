from Learning.Node import Node

class Run(object):
    def __init__(self):
        self.rootNode=None
    
    def insert(self,data):
        if self.rootNode is None:
            self.rootNode=Node(data)
        else:
            self.rootNode.insert(data)
    
    def remove(self,data):
        if self.rootNode:
            if self.rootNode.data==data:
                tempNode=Node(None)
                tempNode.leftChild=self.rootNode
                self.rootNode.remove(data,tempNode)
            else:
                self.rootNode.remove(data,None)
            
    
    
    def traverseInOrder(self):
        if self.rootNode:
            self.rootNode.traverseInOrder()
    
    def getMin(self):
        if self.rootNode:
            return self.rootNode.getMin()