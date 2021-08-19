# Write a program to find the transpose of a square matrix of size N*N. Transpose of a matrix is obtained by changing rows to columns and columns to rows.

class Solution:
    
    #Function to find transpose of a matrix.
    def transpose(self,matrix, n):
       
        
        for i in range(n):
            for j in  range(i,n):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix