# Given a singly linked list: A0→A1→…→An-1→An, reorder it to: A0→An→A1→An-1→A2→An-2→…
# For example: Given 1->2->3->4->5 its reorder is 1->5->2->4->3.

def reorderList(self):
    if (self.head==None or self.head.next==None or self.head.next.next is None):
        return
    head=self.head
    p=None
    fast=head
    while fast is not None and fast.next is not None:
        if p is None:
            p=head
        else:
            p=p.next
        fast=fast.next.next
    
    
    tail=reverse(p.next) 
    
    p.next= None
    p=head
    p1=head
     
    while p1 is not None:
        p=p1
        p1=p.next
        p.next=tail
        tail=tail.next
        p.next.next=p1
        
        
        
    if tail is not None:
        p.next.next=tail
            
    return  
              
      
            
def reverse(head):
    if head is None or head.next is None:
        return head
    
    prev=None
    curr=head
    following=None
    
    while curr is not None:
        following=curr.next
        curr.next=prev
        prev=curr
        curr=following
    
    return prev 