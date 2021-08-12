# Given two singly linked lists of size N and M, write a program to get the point where two linked lists intersect each other.

 
def intersetPoint(head1,head2):
    n=0
    m=0
    p1=head1
    p2=head2
    while p1 is not None:
        p1=p1.next
        n+=1
    while p2 is not None:
        p2=p2.next
        m+=1
    p1=head1
    p2=head2
    if n>m:
        n=n-m
        
        while n!=0:
            p1=p1.next
            n-=1
    else:
        m=m-n
        
        while m!=0:
            p2=p2.next
            m-=1
    
    while p1 is not None:
        if p1 is p2:
            return p1.data
        p1=p1.next
        p2=p2.next
    return -1