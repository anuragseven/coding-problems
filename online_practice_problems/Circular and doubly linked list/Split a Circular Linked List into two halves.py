

class Solution:
    def splitList(self, head, head1, head2):
        if head.next is head:
            
            return head,head
        slow=head
        fast=head.next.next
        
        while fast is not head and fast.next is not head:
            
               
            slow=slow.next
            fast=fast.next.next
        if fast.next is head:
            
            slow=slow.next
          
        t=slow.next
        slow.next=head
        slow=t
        while slow.next is not head:
            slow=slow.next
        
        slow.next=t
        return head,t