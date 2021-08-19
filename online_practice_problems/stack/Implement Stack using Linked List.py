# Let's give it a try! You have a linked list and you have to implement the functionalities push and pop of stack using this given linked list. Your task is to use the class as shown in the comments in the code editor and complete the functions push() and pop() to implement a stack. 

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class MyStack:
    def __init__(self):
        self.head=None
        

    #Function to push an integer into the stack.
    def push(self, data):
        temp=Node(data)
        temp.next=self.head
        self.head=temp
        


    #Function to remove an item from top of the stack.
    def pop(self):
        if self.head is None:
            return -1
        
        result=self.head.data
        self.head=self.head.next
        return result