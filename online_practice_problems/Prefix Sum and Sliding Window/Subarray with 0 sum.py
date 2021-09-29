# Given an array of positive and negative numbers. Find if there is a subarray (of size at-least one) with 0 sum.

class Solution:
    
    #Function to check whether there is a subarray present with 0-sum or not.
    def subArrayExists(self,arr,n):
        s=set()
        
        Sum=0
        
        for num in arr:
            Sum+=num
            
            if Sum in s or Sum==0:
                return True
            
            else:
                s.add(Sum)
                
        return False