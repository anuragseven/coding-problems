# A number N is represented in Linked List such that each digit corresponds to a node in linked list. You need to add 1 to it.

class Solution:
    def addOne(self,head):
        head=self.reverse(head)
        carry=0
        add=1
        p=head
        while p is not None and (add!=0 or carry!=0):
            if (p.data+carry+add) % 10==0:
                p.data=0
                carry=1
                if add==1:
                    add=0
            
            else:
                p.data+=carry+add
                carry=0
                if add==1:
                    add=0
            
            p=p.next
        
        head=self.reverse(head)
        
        
        if carry==1:
            t=Node(1)
            t.next=head
            head=t
        return head
            
    
    def reverse(self,head):
        curr=head
        prev=None
        following=None
        
        while curr is not None:
            following=curr.next
            curr.next=prev
            prev=curr
            curr=following
        return prev