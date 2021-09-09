# Given a sorted array A[] of size N, delete all the duplicates elements from A[].
# Note: Don't use set or HashMap to solve the problem.

class Solution:	
    def remove_duplicate(self, A, N):
	 
        currElement=A[0]
	i=1
	while i<len(A):
	    if currElement==A[i]:
	        A.remove(A[i])
	     else:
	        currElement=A[i]
	        i+=1
        return len(A) 