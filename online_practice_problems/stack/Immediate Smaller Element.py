# Given an integer array Arr of size N. For each element in the array, check whether the right adjacent element (on the next immediate position) of the array is smaller. If next element is smaller, update the current index to that element. If not, then  -1.

class Solution:

    def immediateSmaller(self,arr,n):
        result=[-1]*n
	for i in range(n-1):
	    if arr[i+1]<arr[i]:
	        arr[i]=arr[i+1]
	    else:
	        arr[i]=-1
	arr[-1]=-1