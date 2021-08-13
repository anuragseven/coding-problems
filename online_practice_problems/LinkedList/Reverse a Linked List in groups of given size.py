# Given a linked list of size N. The task is to reverse every k nodes (where k is an input to the function) in the linked list.

class Solution:
    def reverse(self,head, k):
        heads=[]
        start=head
        end=head
        
        while end is not None:
            count=k
            while end is not None and count!=0:
                end=end.next
                count-=1
            
            heads.append(self.reversePart(start,end))
            start=end
                                                                                                                                                                                                                    
        for i in range(len(heads)-1):
            p=heads[i]
            while p.next is not None:
                p=p.next
            p.next=heads[i+1]
        return heads[0]
    
    def reversePart(self,start,end):
        prev=None
        curr=start
        following=None
        while curr is not end:
            following=curr.next
            curr.next=prev
            prev=curr
            curr=following
        return prev

# we have used a stack which will store the nodes of the given linked list. Firstly, push the k elements of the linked list in the stack.
# Now pop elements one by one and keep track of the previously popped node. Point the next pointer of prev node to top element of stack.
# Repeat this process, until NULL is reached.
# This algorithm uses O(k) extra space. 