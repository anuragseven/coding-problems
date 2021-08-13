# Given two linked lists, your task is to complete the function makeUnion(), that returns the union of two linked lists. This union should include all the distinct elements only.

def union(head1,head2):
    s=set()
    p=head1
    
    while p is not None:
        s.add(p.data)
        p=p.next
    
    p=head2
    
    while p is not None:
        s.add(p.data)
        p=p.next
    
    l=list(s)
    l.sort()
    result=Node(0)
    
    p=result
    for val in l:
        p.next=Node(val)
        p=p.next
    result=result.next
    return result