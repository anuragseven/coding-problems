# Given an array A of integers. Find three numbers such that sum of two elements equals the third element and return the triplet in a container result, if no such triplet is found return the container as empty.
def findTriplet(arr,n):
    s=set(arr)
    for val in s:
        l=0
        r=len(arr)-1
        while l<r:
            if arr[l]+arr[r]==val:
                return [arr[l],arr[r],val]
            elif arr[l]+arr[r]>val:
                r-=1
            elif arr[l]+arr[r]<val:
                l+=1
    return [-1]


def findTriplet(arr,n):
    arr.sort()
    k=len(arr)-1
    
    while k>=0:
        i=0
        j=k-1
        while i<j:
            if arr[i]+arr[j]==arr[k]:
                return [arr[i],arr[j],arr[k]]
            elif arr[i]+arr[j]>arr[k]:
                j-=1
            elif arr[i]+arr[j]<arr[k]:
                i+=1
        k-=1
    return [-1]