# Given a matrix mat[][] of size N x M, where every row and column is sorted in increasing order, and a number X is given. The task is to find whether element X is present in the matrix or not.

class Solution:
	def matSearch(self,matrix, N, M, X):
	    r=N-1
	    c=0
	    
	    while c<M:
	        
	        if r<0:
	            return 0
	        if matrix[r][c]==X:
	            return 1
	        
	        if matrix[r][c]>X:
	            r-=1
	        
	        else:
	            if r+1<N and matrix[r+1][c]>X:
	                c+=1
	            elif r+1==N:
	                c+=1
	            else:
	                return 0
           return 0