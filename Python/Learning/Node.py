class Node(object):
    def __init__(self,data):
        self.data=data
        self.leftChild = None
        self.rightChild = None
    
    def insert(self,data):
        if self.data > data:
            if self.leftChild is None:
                self.leftChild=Node(data)
            else:
                self.leftChild.insert(data)
        else:
            if self.rightChild is None:
                self.rightChild=Node(data)
            else:
                self.rightChild.insert(data)
            
    def remove(self,data,ParentNode):
        if self.data > data:
            if self.leftChild is not None:
                self.leftChild.remove(data, self)
        elif self.data > data:
            if self.rightChild is not None:
                self.rightChild.remove(data, self)
        else:
            if self.leftChild is not None and self.rightChild is not None:
                self.data=self.rightChild.getMin()
                self.rightChild.remove(self.data, self)
                
    
    def traverseInOrder(self):
        if self.leftChild is not None:
            self.leftChild.traverseInOrder()
        
        print(self.data)
        
        if self.rightChild is not None:
            self.rightChild.traverseInOrder()
    
    def getMin(self):
        if self.leftChild is None:
            return self.data
        else:
            return self.leftChild.getMin()