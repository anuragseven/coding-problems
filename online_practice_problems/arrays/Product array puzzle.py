#Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

class Solution:
    def productExceptSelf(self, arr, n):
        result=[]
        
        prefix=1
        
        for num in arr:
            result.append(prefix)
            prefix=prefix*num
        
        suffix=1
        
        for i in range(n-1,-1,-1):
            result[i]=result[i]*suffix
            suffix=suffix*arr[i]
            
        return result