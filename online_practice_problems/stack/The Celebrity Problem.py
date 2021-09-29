class Solution:
    
    #Function to find if there is a celebrity in the party or not.
    def celebrity(self, M, n):
        i=0
        j=n-1
        
        while i<j:
            if M[i][j]:
                i+=1
            else:
                j-=1
        
        
        
        for j in range(n):
            if i!=j:
                if M[i][j]==1 or M[j][i]==0:
                    return -1
        return i