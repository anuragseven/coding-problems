# Segregate even and odd nodes in a Link List

class Solution:
    def divide(self, N, head):
        evens=node()
        odds=node()
        p=head
        p1=evens
        p2=odds
        while p is not None:
            if p.data%2==0:
                
                p1.next=node()
                p1.next.data=p.data
                p1=p1.next
            else:
                p2.next=node()
                p2.next.data=p.data
                p2=p2.next
            p=p.next
        evens=evens.next
        odds=odds.next
        
        if evens is None:
            head.next=odds
            head.data=odds.data
            head.next=head.next.next
            return head
        
        p1.next=odds
        head.next=evens
        head.data=evens.data
        head.next=head.next.next
        return head