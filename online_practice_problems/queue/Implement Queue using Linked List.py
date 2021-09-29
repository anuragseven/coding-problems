# Implement a Queue using Linked List. 
# A Query Q is of 2 Types
# (i) 1 x   (a query of this type means  pushing 'x' into the queue)
# (ii) 2     (a query of this type means to pop an element from the queue and print the poped element)

class Node: 
      
    def __init__(self, data): 
        self.data = data 
        self.next = None
        
class MyQueue:
    
    head=None
    last=None
    def push(self, item): 
        if self.head is None:
            self.head=Node(item)
            self.last=self.head
        else:
            self.last.next=Node(item)
            self.last=self.last.next
    
         
         
    def pop(self):
        if self.head is not None:
            value=self.head.data
            self.head=self.head.next
        
            return value
        return -1