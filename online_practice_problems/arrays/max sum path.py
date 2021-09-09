# Given two sorted arrays A and B of size M and N respectively. Each array contains only distinct elements but may have some elements in common with the other array. Find the maximum sum of a path from the beginning of any array to the end of any of the two arrays. We can switch from one array to another array only at the common elements.
# Note: Only one repeated value is considered in the valid path sum.


class Solution:
    def maxSumPath(self,arr1, arr2, m, n):
        maxSum=0
        sum1=0
        sum2=0
        i,j=0,0
        
        while i<m and j<n:
            if arr1[i]>arr2[j]:
                sum2+=arr2[j]
                j+=1
            elif arr1[i]<arr2[j]:
                sum1+=arr1[i]
                i+=1
            else:
                sum1+=arr1[i]
                sum2+=arr2[j]
                maxSum+=max(sum1,sum2)
                sum1=0
                sum2=0
                i+=1
                j+=1
        
        
        if i<m:
            while i<m:
                sum1+=arr1[i]
                i+=1
        
        if j<n:
            while j<n:
                sum2+=arr2[j]
                j+=1
        maxSum+=max(sum1,sum2)
        
        return maxSum