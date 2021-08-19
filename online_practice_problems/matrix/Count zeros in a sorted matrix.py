# Given a N X N binary Square Matrix where each row and column of the matrix is sorted in ascending order. Find the total number of zeros present in the matrix.

class Solution:
    def countZeroes(self, A, N):
        r=N-1
        c=0
        count=0
        while c<N:
            
            while A[r][c]:
                
                if r<0:
                    return count
                
                r-=1
            
            count+=r+1
            c+=1
        return count