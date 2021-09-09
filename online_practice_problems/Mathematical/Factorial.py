# Given a positive integer, N. Find the factorial of N.

class Solution:
    def factorial (self, N):
        if N==0:
            return 1
        
        return N*self.factorial(N-1)


class Solution2:
    def factorial (self, N):
        fact=1
        
        for i in range(N,0,-1):
            fact=fact*i
        return fact