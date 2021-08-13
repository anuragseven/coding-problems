# Clone a linked list with next and random pointer

class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        
        p=head
        while p is not None:
            t=Node(p.data)
            t.next=p.next
            p.next=t
            p=p.next.next
    
        
        p=head
        
        while p is not None:
            if p.arb  is not None:
                p.next.arb=p.arb.next
            p=p.next.next
        
        
        result=head.next
        r=result
        p=head
        
        while True:
            if p.next.next is None:
                p.next=None
                break
            
            t=r.next
            r.next=r.next.next
            p.next=t
            r=r.next
            p=p.next
        return result



# or just use deepcopy :

import copy
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        b=copy.deepcopy(head)
        return b
