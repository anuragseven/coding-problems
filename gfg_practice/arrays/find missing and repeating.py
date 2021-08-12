#Given an unsorted array Arr of size N of positive integers. One number 'A' from set {1, 2, …N} is missing and one number 'B' occurs twice in array. Find these two numbers.

def findTwoElement(arr, n): 
        
        nums=[0]*n
        
        for val in arr:
            nums[val-1]+=1
        
        first,second=None,None
        
        for i in range(n):
            if nums[i]==0:
                first=i+1
            if nums[i]==2:
                second=i+1
        return [second,first]


def findTwoElement( arr, n): 
        first,second=None,None
        for i in range(len(arr)):
            if arr[abs(arr[i])-1]>0:
                arr[abs(arr[i])-1]=-arr[abs(arr[i])-1]
            else:
                second=abs(arr[i])
        
        for i in range(n):
            if arr[i]>0:
                first=i+1
        return [second,first]