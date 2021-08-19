# Given two sorted matrices mat1 and mat2 of size N x N of elements. Given a value x. The problem is to count all pairs from both matrices whose sum is equal to x.

# not optimized O(n3):
class Solution:
	def countPairs(self, mat1, mat2, n, x):
	    count=0
	    
	    for i in range(n):
	        for j in range(n):
	            if (x-mat1[i][j])>0 and self.findElement(mat2,x-mat1[i][j]):
	                count+=1
	                
	    return count
	                
	    
	    
	
	def findElement(self,matrix,X):
	    n=len(matrix)
	    
	    r=n-1
	    c=0
	    
	    while c<n:
	        if r<0:
	            return False
	        
	        if matrix[r][c]==X:
	            return True
	        
	        if matrix[r][c]>X:
	            r-=1
	        
	        else:
	            if r+1<n and matrix[r+1][c]>X:
	                c+=1
	            elif r+1==n:
	                c+=1
	            else:
	                return False
	    return False



# Optimized O(n2):
class Solution:
	def countPairs(self, mat1, mat2, n, X):
	    count=0
	    
	    i=0
	    
	    r=n-1
	    j=0
	    c=n-1
	    
	    while i<n and r>=0:
	        
	        while j<n and c>=0:
	            if mat1[i][j]+mat2[r][c]==X:
	                
	                count+=1
	                j+=1
	                c-=1
	            elif mat1[i][j]+mat2[r][c]>X:
	                c-=1
	            else:
	                j+=1
	        if j==n and c==-1:
	            i+=1
	            r-=1
	            j=0
	            c=n-1
	        elif c==-1:
	            r-=1
	            c=n-1
	        elif j==n:
	            i+=1
	            j=0
	        
	    return count