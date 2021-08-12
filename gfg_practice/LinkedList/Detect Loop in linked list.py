# Given a linked list of N nodes. The task is to check if the linked list has a loop. Linked list can contain self loop.

class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        
        slow=head
        fast=head
        
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            
            if slow is fast:
                return True
        return False