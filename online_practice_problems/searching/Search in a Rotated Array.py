# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. The task is to find the index of the given element key in the array A.

class Solution:
    def search(self, arr : list, l : int, h : int, key : int):
        
        pivot=self.findPivot(arr,0,len(arr)-1)
        i=self.binarySearch(arr,0,pivot,key)
        if i==-1:
            i=self.binarySearch(arr,pivot+1,len(arr)-1,key)
        
        return i
        
    def binarySearch(self,arr,l,r,x):
        while l<=r:
            mid=l+(r-l)//2
            if arr[mid]==x:
                return mid
            if arr[mid]>x:
                r=mid-1
            else:
                l=mid+1
        return -1
        
    def findPivot(self,arr,l,h):
        if h<l:
            return -1
        if l==h:
            return l
        
        mid=(l+h)//2
        
        if mid<h and arr[mid]>arr[mid+1]:
            return mid
        if mid>l and arr[mid]<arr[mid-1]:
            return mid-1
        if arr[l]>=arr[mid]:
            return self.findPivot(arr,l,mid-1)
        return self.findPivot(arr,mid+1,h)



class Solution:
    def search(self, A : list, l : int, h : int, key : int):
        return self. modifiedBinarySearch(A,key)
        
    
    
    def modifiedBinarySearch(self,A,X):
        
        l=0
        r=len(A)-1
        
        while l<=r:
            mid=l+(r-l)//2
            
            if A[mid]==X:
                return mid
            
            if A[l]<=A[mid]:
                if X>=A[l] and X<A[mid]:
                    r=mid-1
                else:
                    l=mid+1

                
            
            elif X>A[mid] and X<=A[r]:
                l=mid+1
            else:
                r=mid-1
                
        return -1

