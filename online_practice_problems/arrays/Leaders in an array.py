# Given an array A of positive integers. Your task is to find the leaders in the array. An element of array is leader if it is greater than or equal to all the elements to its right side. The rightmost element is always a leader. 

class Solution:
    
    def leaders(self, A, N):
        currMax=A[-1]
        result=[]
        for i in range(N-1,-1,-1):
            if A[i]>=currMax:
                currMax=A[i]
                result.append(A[i])
        result=result[::-1]
        
        return result