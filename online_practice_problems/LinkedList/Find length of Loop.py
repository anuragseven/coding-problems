# Given a linked list of size N. The task is to complete the function countNodesinLoop() that checks whether a given Linked List contains a loop or not and if the loop is present then return the count of nodes in a loop or else return 0. C is the position of the node to which the last node is connected. If it is 0 then no loop.

def countNodesinLoop(head):
    
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        
        if slow is fast:
            p=slow
            slow=slow.next
            count=1
            while slow is not p:
                slow=slow.next
                count+=1
            return count
    return 0