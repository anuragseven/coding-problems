# Given a boolean matrix of size RxC where each cell contains either 0 or 1, modify it such that if a matrix cell matrix[i][j] is 1 then all the cells in its ith row and jth column will become 1.

def booleanMatrix(matrix):
    r=len(matrix) 
    c=len(matrix[0])
    
    pairs=[]
    
    for i in range(r):
        for j in range(c):
            if matrix[i][j]==1:
                pairs.append([i,j])

    
    for i,j in pairs:
        matrix[i]=[1]*c
        makeColumnOne(r,j)

def makeColumnOne(r,j):
    for i in range(r):
        matrix[i][j]=1