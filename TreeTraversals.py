def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getleftChild())
        preorder(tree.getrightChild())
        
def inorder(tree):
    if tree:
        inorder(tree.getleftChild())
        print(tree.getRootVal())
        inorder(tree.getrightChild())
        
def postorder(tree):
    if tree:
        postorder(tree.getleftChild())
        postorder(tree.getrightChild())
        print(tree.getRootVal())
      
tree = BinaryTree(3)
tree.insertLeft(1)
tree.insertLeft(2)
tree.insertRight(4)
inorder(tree)
preorder(tree)
postorder(tree)
