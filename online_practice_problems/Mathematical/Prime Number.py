# For a given number N check if it is prime or not. A prime number is a number which is only divisible by 1 and itself.

class Solution:
    def isPrime (self, N):
        if N==1:
            return 0
        for i in range(2,int(N**0.5)+1):
            if N%i==0:
                return 0
        
        return 1