# Given N, count all ‘a’(>=1) and ‘b’(>=0) that satisfy the condition a3 + b3 = N.

class Solution:
    def pairCubeCount(self, N):
        if self.isCube(N):
            count=-1
        else:
            count=0
        n=int((N**(1/3))+1)
        
        for i in range(n):
            if self.isCube(N-i**3):
                count+=1
        return count    
    
    
    def isCube(self,N):
        n=round(N**(1/3))
        
        if n**3 ==N:
            return True
        return False