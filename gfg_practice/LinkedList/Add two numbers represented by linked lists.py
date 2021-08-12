# Given two numbers represented by two linked lists of size N and M. The task is to return a sum list.

# The sum list is a linked list representation of the addition of two input numbers from the last.

class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        p1=first
        p2=second
        num1=''
        num2=''
        while p1 is not None:
            num1+=str(p1.data)
            p1=p1.next
        while p2 is not None:
            num2+=str(p2.data)
            p2=p2.next
        num=int(num1)+int(num2)
        num=str(num)
        
        result=Node(0)
        p=result
        for c in num:
            p.next=Node(int(c))
            p=p.next
        result=result.next
        return result