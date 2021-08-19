# Given an array with positive number the task to find the largest subsequence from array that contain elements which are Fibonacci numbers.

class Solution:
    def getMaxandMinProduct(self, arr, n):
        
        
        
        fibs=self.getFibonacciNumbers(max(arr))
        
            
        result=[]
        for val in arr:
            if val in fibs:
                result.append(val)
        return result
    
        
    
    def getFibonacciNumbers(self,m):
        s=set()
        
        if m<=0:
            return s
        if m==1:
            s.add(0)
            return s
        
        prev=0
        curr=1
        s.add(prev)
        s.add(curr)
        while(curr < m):
            
            temp = prev+curr
            prev = curr
            curr = temp
            s.add(curr)
        
        return s