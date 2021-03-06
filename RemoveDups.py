def removeDups(ll):
    
    if ll.head is None:
        return
    
    current = ll.head
    seen = set([current.value])
    while(current.next):
        if current.next.value in seen:
            current.next = current.next.next
            
        else:
            seen.add(current.next.value)
            current = current.next
            
    return ll

def removeDups_followup(ll):
    
    if ll.head is None:
        return
    
    current = ll.head
    while current:
        runner = current.next
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
                
            else:
                runner = runner.next
                
        current = current.next
            
    return ll.head

    
    

