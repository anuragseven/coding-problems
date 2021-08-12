#Given an array arr[] of N non-negative integers representing the height of blocks. If width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. 
def trappingWater(self, arr,n):
        left=[0]*n
        right=[0]*n
        
        left[0]=arr[0]
        for i in range(1,len(arr)):
            left[i]=max(left[i-1],arr[i])
        
        right[-1]=arr[-1]
        
        for i in range(n-2,-1,-1):
            right[i]=max(right[i+1],arr[i])
        
        maxWater=0
        
        for i in range(len(arr)):
            maxWater+=min(right[i],left[i])-arr[i]
            
        return maxWater