# Given a doubly linked list and a position. The task is to delete a node from given position in a doubly linked list.
class Solution:
    def deleteNode(self,head, x):
        if x==1:
            if head.next is None:
                return
            head=head.next
            head.prev=None
            return head
        
        p=head
        x-=2
        while p is not None and x!=0:
            p=p.next
            x-=1
        if p is None:
            return head
        
        if p.next.next is None:
            p.next=None
            return head
        
        p.next=p.next.next
        p.next.prev=p
        return head