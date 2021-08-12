# Given a singly linked list of size N. The task is to swap elements in the linked list pairwise.
# For example, if the input list is 1 2 3 4, the resulting list after swaps will be 2 1 4 3.
# Note: You need to swap the nodes, not only the data. If only data is swapped then driver will print -1.

class Solution:    
    def pairWiseSwap(self, head):
        if head.next is None:
            return head
        node=Node(0)
        n=node
        n.next=head
        p=head
        q=head.next
        while p is not None and q is not None:
            p.next=q.next
            q.next=p
            n.next=q
            n=p
            p=p.next
            if p is not None:
                q=p.next
        return node.next