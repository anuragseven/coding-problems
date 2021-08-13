# Given a sorted doubly linked list and an element X, your need to insert the element X into correct position in the sorted DLL.

def sortedInsert(head, x):
    if x<head.data:
        t=Node(x)
        t.next=head
        head.prev=t
        return t
    
    p=head 
    while p.next is not None and p.next.data<x:
        p=p.next
    
    t=Node(x)
    t.next=p.next
    if p.next is not None:
        p.next.prev=t
    t.prev=p
    p.next=t
    return head