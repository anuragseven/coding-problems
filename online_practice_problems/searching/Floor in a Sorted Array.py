# Given a sorted array arr[] of size N without duplicates, and given a value x. Floor of x is defined as the largest element K in arr[] such that K is smaller than or equal to x. Find the index of K(0-based indexing).
def findFloor(A,N,X):
        prev=0
        for i in range(len(A)):
            if A[i]==X:
                return i
            elif A[i]>X:
                break
            else:
                prev=i
        if A[prev]<X:
            return prev
        return -1


class Solution:
    #User function Template for python3
    
    #Complete this function
    def findFloor(self,A,N,X):
        index=self.binarySearch(A,X)
        
        if A[index]>X:
            return index-1
        return index
     
    def binarySearch(self,a, num):
        l = 0
        r = len(a) - 1
        mid=0
        while l <= r:
            mid = l+(r-l)//2
            if a[mid] == num:
                return mid
            if a[mid] < num:
                l = mid + 1
            else:
                r = mid - 1
        return mid