# Given a linked list, delete N nodes after skipping M nodes of a linked list until the last of the linked list.

def skipMdeleteN(self, head, M, N):
        
        count=1
        t=head
        
        
        while t is not None:
            if count%M==0:
                i=N
                while i!=0 and t.next is not None:
                    t.next=t.next.next
                    i-=1
                    
            count+=1
            t=t.next