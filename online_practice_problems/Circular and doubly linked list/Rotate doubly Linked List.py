# Given a doubly linked list, rotate the linked list counter-clockwise by P nodes. Here P is a given positive integer and is smaller than the count of nodes(N) in a linked list.

def update(llist, p):
    head=llist.head
    if p==0:
        return head
    k=p
    p-=1
    count=0
    p1=head
    while p1 is not None and p!=0:
        p1=p1.next
        p-=1
        count+=1
    
    if p1 is None:
        k=k%count
        if k==0:
            return head
        p1=head
        k-=1
        while p1 is not None and k!=0:
            p1=p1.next
            k-=1
        
    
    result=p1.next
    p1.next=None
    result.prev=None
    r=result
    while r.next is not None:
        r=r.next
    
    r.next=head
    head.prev=r
    llist.head=result
    return llist