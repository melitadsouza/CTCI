class Node(object):
    
    def __init__(self,value):
        
        self.value = value
        #self.prevnode = None
        self.nextnode = None
        
    def loopDetect(node):
        
        slow = node
        fast = node
        
        while fast != None and fast.nextnode != None:
            slow = slow.nextnode
            fast = fast.nextnode.nextnode
            if slow == fast:
                break
                
        if fast == None or fast.nextnode == None:
            return
        
        slow = node
        while slow != fast:
            slow = slow.nextnode
            fast = fast.nextnode
        return fast
