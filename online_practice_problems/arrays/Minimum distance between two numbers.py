# You are given an array A, of N elements. Find minimum index based distance between two elements of the array, x and y.

class Solution:
    def minDist(self, arr, n, x, y):
        diff=float('inf')
        
        j=-1
        
        for i in range(n):
            if arr[i]==x or arr[i]==y:
                if j!=-1 and arr[i]!=arr[j]:
                    diff=min(diff,i-j)
                
                j=i
        
        return diff if diff!=float('inf') else -1  