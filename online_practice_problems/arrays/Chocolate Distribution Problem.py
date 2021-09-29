# Given an array A[ ] of positive integers of size N, where each value represents the number of chocolates in a packet. Each packet can have a variable number of chocolates. There are M students, the task is to distribute chocolate packets among M students such that :
# 1. Each student gets exactly one packet.
# 2. The difference between maximum number of chocolates given to a student and minimum number of chocolates given to a student is minimum.

class Solution:

    def findMinDiff(self, A,N,M):

        A.sort()
        l=0
        r=M-1
        cmin=(10**9)+1
        
        while r<N:
            cmin=min(cmin,A[r]-A[l])
            l+=1
            r+=1
        
        return cmin