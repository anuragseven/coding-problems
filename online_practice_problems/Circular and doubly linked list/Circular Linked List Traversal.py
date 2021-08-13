

class Node:
    
    def __init__(self,data=None):
        self.data=data
        self.next=None
# Given a circular linked list, your task is to complete the method printList() that prints the linked list.        

class CircularLinkedList: 
    head=None
    last=None
    def push(self,data):
        if self.head is None:
            self.head=Node(data)
            self.head.next=self.head
            self.last=self.head
        else:
            t=Node(data)
            t.next=self.head
            self.last.next=t
            self.head=t
            
        
        
        
    #  Function to print nodes in a given Circular linked list     
    def printList(self):
        
        l=[]
        l.append(self.head.data)
        p=self.head.next
        while p is not self.head:
            l.append(p.data)
            p=p.next
        print(*l)