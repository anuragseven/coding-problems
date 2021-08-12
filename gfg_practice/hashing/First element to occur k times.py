# Given an array of N integers. Find the first element that occurs K number of times. 
def firstElementKTime(self,  a, n, k):
        nums={}
        
        for i,num in enumerate(a):
            if num in nums and nums[num][0]<k:
                nums[num][0]+=1
                nums[num][1]=i
            
            elif num not in nums:
                nums[num]=[1,i]
        minIndex=len(a)
        for num in a:
            if nums[num][0]==k:
                
                minIndex=min(minIndex,nums[num][1])
        
        return a[minIndex] if minIndex!=len(a) else -1