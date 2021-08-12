 #Given an array of n distinct elements. Find the minimum number of swaps required to sort the array in strictly increasing order.   
    def minSwaps(self, nums):
	    temp=list(nums)
	    temp.sort()
	    indices={}
	    for i in range(len(nums)):
	        indices[nums[i]]=i
	    
	    swaps=0
	    for i in range(len(nums)):
	        if nums[i]!=temp[i]:
	            val=nums[i]
	            swaps+=1
	            
	            nums[i],nums[indices[temp[i]]]=nums[indices[temp[i]]],nums[i]
	            indices[val]=indices[temp[i]]
	            indices[nums[i]]=i
	    return swaps