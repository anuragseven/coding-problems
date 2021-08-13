# Given a doubly-linked list, a position p, and an integer x. The task is to add a new node with value x at the position just after pth node in the doubly linked list.

def addNode(head, p, data):
    p1=head
    while p1.next is not None and p!=0:
        p1=p1.next
        p-=1
    
    t=Node(data)
    t.next=p1.next
    p1.next=t
    t.prev=p1 