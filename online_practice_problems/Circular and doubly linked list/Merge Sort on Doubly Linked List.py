# Given Pointer/Reference to the head of a doubly linked list of N nodes, the task is to Sort the given doubly linked list using Merge Sort in both non-decreasing and non-increasing order.

def merge(h1,h2):
    if h1.data<h2.data:
        p1=h1
        p2=h2
    else:
        p1=h2
        p2=h1
    
    while p1.next is not None and p2 is not None:
        if p1.next.data<p2.data:
            p1=p1.next
        else:
            t=p2.next
            if t is not None:
                t.prev=None
            p2.next=p1.next
            p1.next.prev=p2
            p1.next=p2
            p2.prev=p1
            p2=t
            p1=p1.next
    while p1.next is not None:
        p1=p1.next
    p1.next=p2
    if p2 is not None:
        p2.prev=p1
    return h1 if h1.data<h2.data else h2
    
def divide(head):
    
    if head is None or head.next is None:
        return head
    
    slow=None
    fast=head
    while fast is not None and fast.next is not None:
        if slow is None:
            slow=head
        else:
            slow=slow.next
        fast=fast.next.next
    
    t=slow.next
    slow.next=None
    t.prev=None
    
    h1=divide(head)
    h2=divide(t)
    return merge(h1,h2)
    
def sortDoubly(head):
    return divide(head)  