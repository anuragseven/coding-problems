# Given two numbers A and B. The task is to find out their LCM and GCD

class Solution:
    def lcmAndGcd(self, A , B):
        gcd=self.gcd(A,B)
        lcm=(A*B)//gcd
        
        return [lcm,gcd]
    
    
    def gcd(self,A,B):
        if A==0:
            return  B
        
        return self.gcd(B%A,A)