# Given a sorted array Arr of size N and a number X, you need to find the number of occurrences of X in Arr.
class Solution:

	def count(self,arr, n, x):
	    index=self.binarySearch(arr,x)
	    if index==-1:
	        return 0
	    
	    count=1
	    r=index+1
	    l=index-1
	    while  r<len(arr) and arr[r]==x:
	        count+=1
	        r+=1
	    while  l>=0 and arr[l]==x:
	        count+=1
	        l-=1
	    return count
	    
	    
    def binarySearch(self,arr,x):
        l=0
        r=len(arr)-1
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==x:
                return mid
            if arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return -1