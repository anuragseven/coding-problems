# Given a number N.Check whether it is a triangular number or not.
# Note: A number is termed as a triangular number if we can represent it in the form of a triangular grid of points such that the points form an equilateral triangle and each row contains as many points as the row number, i.e., the first row has one point, the second row has two points, the third row has three points and so on.
# The starting triangular numbers are 1, 3 (1+2), 6 (1+2+3), 10 (1+2+3+4).

# Hint: The triangular number is the sum of first n natural numbers
class Solution:
    def isTriangular(self, N): 
        S=0
        n=1
        
        while S<N:
            S+=n
            if S==N:
                return 1
            
            n+=1
        return 0



from math import floor
class Solution:
    def isTriangular(self, N): 
        a=1
        b=1
        c=-2*N
        
        D=(b**2)-4*a*c
        if D<0:
            return 0
        r1=(-b+D**0.5)/2*a
        r2=(-b-D**0.5)/2*a
        
        if r1>0 and floor(r1)==r1:
            return 1
        
        if r2>0 and floor(r2)==r2:
            return 1
        
        return 0