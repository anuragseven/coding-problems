# Given Pointer/Reference to the head of the linked list, the task is to Sort the given linked list using Merge Sort.

class Solution:
    #Function to sort the given linked list using Merge Sort.
    def mergeSort(self, head):
        return self.divide(head)         
    
    
    
    def divide(self,p):
        if p is None or p.next is None:
            return p
        slow=None
        fast=p
        while fast is not None and fast.next is not None:
            if slow is None:
                slow=p
            else:
                slow=slow.next
                
            fast=fast.next.next
            
        
        
        t=slow.next
        slow.next=None
        slow=t
        p1=self.divide(p)
        p2=self.divide(slow)
        return self.merge(p1,p2)
        
        
    
    
    def merge(self,head1,head2):
        if head1.data<=head2.data:
            p1=head1
            p2=head2
        else:
            p1=head2
            p2=head1
        
        while p1.next is not None and p2 is not None:
            if p1.next.data<p2.data:
                p1=p1.next
            else:
                t=p2.next
                p2.next=p1.next
                p1.next=p2
                p2=t
                p1=p1.next
        while p1.next is not None:
            p1=p1.next
        p1.next=p2
        return head1 if head1.data<=head2.data else head2