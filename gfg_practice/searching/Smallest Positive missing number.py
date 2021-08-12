# You are given an array arr[] of N integers including 0. The task is to find the smallest positive number missing from the array.


class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        if len(arr)==1:
           if arr[0]==1:
               return 2
           else:
               return 1
        i=self.segregate(arr,n)
        arr=arr[i:]
        for i in range(len(arr)):
            if abs(arr[i])-1<len(arr):
                if arr[abs(arr[i])-1]>0:
                    arr[abs(arr[i])-1]=-1*arr[abs(arr[i])-1]
        
        
        for i in range(len(arr)):
            if arr[i]>0:
                return i+1
                
        
        return len(arr)+1
        
    
    def segregate(self,arr, size):
        j = 0
        for i in range(size):
            if (arr[i] <= 0):
                arr[i], arr[j] = arr[j], arr[i]
                j += 1 # increment count of non-positive integers
        return j