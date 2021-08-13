# Given a sorted array containing only 0s and 1s, find the transition point. 

def transitionPoint(arr, n):
    if arr[0]==1:
       return 0
    return search(arr)
def search(arr):
    l=0
    r=len(arr)-1
    
    while l<=r:
        mid=l+(r-l)//2
        if arr[mid-1]==0 and arr[mid]==1:
            return mid
        
        
        if arr[mid-1]==0 and arr[mid]==1:
            return mid
        if arr[mid-1]==0 and arr[mid]==0:
            l=mid+1
        
        elif arr[mid]==1:
            r=mid-1
        
    return -1   