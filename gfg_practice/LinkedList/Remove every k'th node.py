# Given a singly linked list, your task is to remove every kth node from the linked list.
def deleteK(head, k):
    if head.next is None and k==1:
        return None
    if k==0:
        return head
    if k==1:
        return 
        
    t=head
    count=1
    while t is not None:
        if (count+1) % k==0 and t.next is not None:
            t.next=t.next.next
            count+=1
        t=t.next
        count+=1
    return head