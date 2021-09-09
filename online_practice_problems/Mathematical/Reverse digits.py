# Given N,  reverse the digits of N.

class Solution:
	def reverse_digit(self, n):
	    arr=[]
	    while n!=0:
	        d=n%10
	        arr.append(d)
	        n=n//10
	    
	    result=0
	    
	    t=1
	    for i in range(len(arr)-1,-1,-1):
	        result+=arr[i]*t
	        t*=10
	    return result