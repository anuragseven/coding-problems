# Given a singly linked list consisting of N nodes. The task is to remove duplicates (nodes with duplicate values) from the given list (if exists).
# Note: Try not to use extra space. Expected time complexity is O(N). The nodes are arranged in a sorted way.


def removeDuplicates(head):
    if head.next is None:
        return 
    prev=head.data
    p=head
    while p.next is not None:
        if prev!=p.next.data:
            prev=p.next.data
            p=p.next
        else:
            p.next=p.next.next
            
            
    return head