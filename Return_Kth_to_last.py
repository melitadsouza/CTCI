class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        #self.prevnode = None
        self.nextnode = None

def kth_to_last(k,head):
    
    left_pointer = head
    right_pointer = head
    
    for i in range(k):
        if right_pointer.nextnode is None:
            raise LookupError('Error:k is larger than LinkedList')
        right_pointer = right_pointer.nextnode
        
    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
        
    return left_pointer
     
a = Node(1)
b = Node(2)
c = Node(3)
d= Node(4)
e = Node(5)
a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = e
kth_to_last(4,a)

    
    
    
    
