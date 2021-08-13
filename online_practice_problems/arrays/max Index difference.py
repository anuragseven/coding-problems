#Given an array A[] of N positive integers. The task is to find the maximum of j - i subjected to the constraint of A[i] <= A[j].

# TC=O(n) and SC=O(n)
def maxIndexDiff(self,arr, n): 
        
        minLeft=[]
        maxRight=[0]*n
        
        maxNum=-1
        for i in range(n-1,-1,-1):
            maxNum=max(maxNum,arr[i])
            maxRight[i]=maxNum
        minNum=10**6
        
        for val in arr:
            minNum=min(minNum,val)
            minLeft.append(minNum)
            
        maxIndDiff=0
        
        i=j=0
        while i<n and j<n:
            if minLeft[i]<=maxRight[j]:
                maxIndDiff=max(maxIndDiff,j-i)
                j+=1
            
            else:
                i+=1
        
        return maxIndDiff