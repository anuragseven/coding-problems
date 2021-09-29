# Given an array arr[ ] of size N having distinct elements, the task is to find the next greater element for each element of the array in order of their appearance in the array.
# Next greater element of an element in the array is the nearest element on the right which is greater than the current element.
# If there does not exist next greater of current element, then next greater element for current element is -1. For example, next greater of the last element is always -1.

class Solution:
    def nextLargerElement(self,arr,n):
        result=[-1]*n
        
        stack=[0]
        for i in range(1,n):
            if arr[i]<arr[stack[-1]]:
                stack.append(i)
                
            else:
                while stack!=[] and arr[stack[-1]]<arr[i]:
                    result[stack.pop()]=arr[i]
                
                stack.append(i)
        
        while stack!=[]:
            result[stack.pop()]=-1
        return result