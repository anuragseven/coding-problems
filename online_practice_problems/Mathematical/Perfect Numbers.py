# Given a number N, check if a number is perfect or not. A number is said to be perfect if sum of all its factors excluding the number itself is equal to the number.

class Solution:
    def isPerfectNumber(self, n):
        if n==1:
            return 0
        S=1
        i=2
        while i*i<=n:
            if N%i==0:
                S=S+i+n//i
            i+=1
        
        if S==n:
            return 1
        return 0