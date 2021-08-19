# Given a matrix of size N x N. Print the elements of the matrix in the snake like pattern depicted below.
# image: https://contribute.geeksforgeeks.org/wp-content/uploads/snake-pattern.jpg
class Solution:
    
    #Function to return list of integers visited in snake pattern in matrix.
    def snakePattern(self, matrix): 
       n=len(matrix)
       result=[]
       j=0
       flag=True
       for i in range(n):
           j=0 if flag else -1
           while j<n if flag else j>=-n:
               result.append(matrix[i][j])
               if flag:
                   j+=1
               else:
                   j-=1
           flag=False if flag else True
       return result