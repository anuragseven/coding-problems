# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that has the maximum number of 1's.

class Solution:

    def rowWithMax1s(self,arr, n, m):
        maxRow=-1
	maxOnes=0
	for i in range(n):
	    for j in range(m):
	        if arr[i][j]==1:
	            if m-j>maxOnes:
	                maxOnes=m-j
	                maxRow=i
        return maxRow