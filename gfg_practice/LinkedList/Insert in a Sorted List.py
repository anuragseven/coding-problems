# Given a sorted singly linked list and a data, your task is to insert the data in the linked list in a sorted way i.e. order of the list doesn't change.

class Solution:
    def sortedInsert(self, head,key):
        if key<=head.data:
            t=Node(key)
            t.next=head
            head=t
            return head
    
        p=head
        while p.next is not None and p.next.data<key:
            p=p.next
    
    
        t=Node(key)
        t.next=p.next
        p.next=t
        return head