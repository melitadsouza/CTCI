class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        self.nextnode = None
        
    def del_middle_node(node):
        node.value = node.nextnode.value
        node.nextnode = node.nextnode.nextnode
        
        
a = Node(1)
b = Node(2)
c = Node(3)
a.nextnode = b
b.nextnode = c
del_middle_node(b)
