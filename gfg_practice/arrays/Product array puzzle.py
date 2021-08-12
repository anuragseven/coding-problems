#Given an array nums[] of size n, construct a Product Array P (of same size n) such that P[i] is equal to the product of all the elements of nums except nums[i].

# using division operation
def productExceptSelf(self, nums, n):
        result=[]
        zeroCount=0
        zeroIndex=-1
        product=1
        for i,val in enumerate(nums):
            if val!=0:
                product*=val
            if val==0:
                zeroCount+=1
                zeroIndex=i
                
        if zeroCount==1:
            
            result=[0]*n
            result[zeroIndex]=product
            return result
        elif zeroCount>1:
            return [0]*n
        
        for val in nums:
            
            result.append(int(product/val))
        
        return result


# TC=O(n) , SC=O(n)
def productExceptSelf( nums, n):
        prefix=[1]*n
        suffix=[1]*n
        product=[]
        for i in range(1,n):
            prefix[i]=arr[i-1]*prefix[i-1]
        
        for i in range(n-2,-1,-1):
            suffix[i]=arr[i+1]*suffix[i+1]
        
        
        for i in range(n):
            product.append(suffix[i]*prefix[i])
            
        return product


# optimised
def productExceptSelf(self, nums, n):
       
        product=[1]*n
        temp=1
        for i in range(0,n):
            product[i]=temp
            temp*=arr[i]
        
        temp=1
        for i in range(n-1,-1,-1):
            product[i]*=temp
            temp*=arr[i]
        
            
        return product