# Given an array of distinct integers. The task is to count all the triplets such that sum of two elements equals the third element.

def countTriplet(self, arr, n):
		arr.sort()
		
		k=len(arr)-1
		count=0
		while k>=0:
		    num=arr[k]
		    l=0
		    r=len(arr)-1
		    while l<r:
		        if arr[l]+arr[r]==num:
		            count+=1
		            r-=1
		        elif arr[l]+arr[r]>num:
		            r-=1
		        elif arr[r]+arr[l]<num:
		            l+=1
		    k-=1
	    return count