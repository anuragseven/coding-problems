# Write a program to calculate nPr. nPr represents n permutation r and value of nPr is (n!) / (n-r)!.

class Solution:
    def nPr(self, n, r):
        return self.factorial(n)//self.factorial(n-r)
    
    def factorial(self,n):
        
        fact=1
        for i in range(n,0,-1):
            fact=fact*i
        return fact