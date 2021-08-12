# Given a singly linked list of N nodes. The task is to find the middle of the linked list. For example, if given linked list is 1->2->3->4->5 then the output should be 3.
# If there are even nodes, then there would be two middle nodes, we need to print the second middle element. For example, if given linked list is 1->2->3->4->5->6 then the output should be 4.
def findMid(head):
    if head.next is None:
        return head.data
    slow=head
    fast=head
    
    while fast.next is not None and fast.next.next is not None:
        slow=slow.next
        fast=fast.next.next
    
    if fast.next is None:
        
        return slow.data
    
    if fast.next.next is None:
        slow=slow.next
        return slow.data