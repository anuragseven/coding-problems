# Given a Binary Number B, find its decimal equivalent.

class Solution:
	def binary_to_decimal(self, s):
	    n=len(s)-1
	    result=0
	    for i in range(n+1):
	        result+=int(s[i])*(2**(n-i))
        return result