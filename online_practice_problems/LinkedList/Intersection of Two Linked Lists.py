# Given two linked lists, the task is to complete the function findIntersection(), that returns the intersection of two linked lists. Each of the two linked list contains distinct node values.

class Solution:
    def findIntersection(self, head1, head2):
     s2=set()
     
     p1=head1
     p2=head2
     
     
     while p2 is not None:
         s2.add(p2.data)
         p2=p2.next
     
     
     result=Node(0)
     p=result
     while p1 is not None:
         if p1.data in s2:
             p.next=Node(p1.data)
             p=p.next
         p1=p1.next
     result=result.next
     return result