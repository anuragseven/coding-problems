# Given a singly linked list of size N of integers. The task is to check if the given linked list is palindrome or not.

class Solution:
    def isPalindrome(self, head):
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
        tail= self.reverse(slow)
        p=head
        while p is not None and tail is not None :
            
            if p.data!=tail.data:
                return False
            p=p.next
            tail=tail.next
        return True
        
    def reverse(self,start):
        prev=None
        curr=start
        following=None
        while curr is not None:
            following=curr.next
            curr.next=prev
            prev=curr
            curr=following
        return prev