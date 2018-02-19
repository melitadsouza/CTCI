class BinaryTree(object):
    
    def __init__(self,rootObj):
        
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None
        
    def insertLeft(self,newNode):
        # if left child doesn't exist
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            #if left child exists
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t
    
    def insertRight(self,newNode):
        # if right child doesn't exist
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            #if right child exists
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t
    
    def getrightChild(self):
        return self.rightChild
    
    def getleftChild(self):
        return self.leftChild
    
    def setRootVal(self,newVal):
        self.key = newVal
        
    def getRootVal(self):
        return self.key
        
r = BinaryTree('a')
r.getRootVal()
r.insertLeft('b')
r.insertRight('c')
r.getleftChild().getRootVal()
r.getrightChild().getRootVal()
