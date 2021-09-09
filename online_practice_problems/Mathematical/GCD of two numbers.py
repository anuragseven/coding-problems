# Given two positive integers A and B, find GCD of A and B.


class Solution:
    def gcd(self, A, B):
        
        if A==0:
            return B
        return self.gcd(B%A,A)