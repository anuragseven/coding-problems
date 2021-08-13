# A peak element in an array is the one that is not smaller than its neighbours.
# Given an array arr[] of size N, find the index of any one of its peak elements
class Solution:   
    def peakElement(self,arr, n):
        if len(arr)==1:
            return 0
        result=self.search(arr,0,len(arr)-1)
        
        return result
    def search(self,arr,l,r):
        
                
        while l<=r:
            mid=l+(r-l)//2
            
            if (mid==0 or arr[mid-1]<=arr[mid]) and (mid==len(arr)-1 or arr[mid]>=arr[mid+1]):
                return mid
            
            if mid>0 and arr[mid-1]>arr[mid]:
                r=mid-1
            
            else:
                l=mid+1
                