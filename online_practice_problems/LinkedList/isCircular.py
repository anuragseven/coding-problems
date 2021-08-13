# Given head, the head of a singly linked list, find if the linked list is circular or not. A linked list is called circular if it not NULL terminated and all nodes are connected in the form of a cycle. An empty linked list is considered as circular.

def isCircular(head):
    
    p=head
    p1=head.next
    while p1 is not None and p1 is not p:
        p1=p1.next
    
    if p1 is None:
        return False
    return True