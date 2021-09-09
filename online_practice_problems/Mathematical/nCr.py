# Given two integers n and r, find nCr. Since the answer may be very large, calculate the answer modulo 109+7.

class Solution:
    def nCr(self, n, r):
        if r>n:
            return  0
        M=(10**9)+7
        nf=self.factorial(n)
        
        rf=self.factorial(r)
        nrf=self.factorial(n-r)
        
        return (nf//(rf*nrf))%M
    
    
    def factorial(self,N):
        fact=1
        
        for i in range(N,0,-1):
            fact=fact*i
        return fact