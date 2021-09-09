# Given an array of N positive integers, find GCD of all the array elements.

class Solution:
    def gcd(self, n, arr):
        
        currgcd=arr[0]
        
        for num in arr:
            currgcd=self.gcdOfTwo(currgcd,num)
        return currgcd    
            
    
    def gcdOfTwo(self,A,B):
        if A==0:
            return B
        return self.gcdOfTwo(B%A,A)