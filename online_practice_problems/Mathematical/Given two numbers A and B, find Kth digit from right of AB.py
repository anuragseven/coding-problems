

class Solution:
    def kthDigit(self, A, B, K):
        N=A**B
        
        d=0
        c=0
        
        while N!=0:
            d=N%10
            c+=1
            if c==K:
                return d
            N=N//10