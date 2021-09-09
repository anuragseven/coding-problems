# Given two positive numbers X and Y, check if Y is a power of X or not.

class Solution:
    def isPowerOfAnother (ob,X,Y):
        if X==1:
            return 1 if Y==1 else 0
        
        powr=1
        
        while powr<Y:
            powr=powr*X
        
        return 1 if powr==Y else 0