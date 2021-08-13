# Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.

def sortedMerge(head1, head2):
    if head1.data<=head2.data:
        
        p1=head1
        p2=head2
    else:
        p1=head2
        p2=head1
  
    
    while p1.next is not None and p2 is not None:
        
        
        if p1.next.data<=p2.data:
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

