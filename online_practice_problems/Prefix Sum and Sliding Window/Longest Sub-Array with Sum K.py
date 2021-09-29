# Given an array containing N integers and an integer K., Your task is to find the length of the longest Sub-Array with the sum of the elements equal to the given value K.

class Solution:
    def lenOfLongSubarr (self, A, N, k) : 
        
        d={}
        
        maxLen=0
        
        S=0
        
        for i in range(len(A)):
            
            S+=A[i]
            
            if S==k:
                maxLen=i+1
                
            
            elif S-k in d:
                maxLen=max(maxLen,i-d[S-k])
            
            if S not in d:
                d[S]=i
            
        
        return maxLen