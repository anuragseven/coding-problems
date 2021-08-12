# Given a sorted and rotated array A of N distinct elements which is rotated at some point, and given an element key. The task is to find the index of the given element key in the array A.
class Solution:
    def search(self, arr : list, l : int, h : int, key : int):
        prev=0
        for i in range(len(arr)):
            if arr[i]==key:
                return i
            elif arr[i]<arr[prev]:
                break
            else:
                prev=i
        
        i=self.binarySearch(arr,0,prev,key)
        if i==-1:
            i=self.binarySearch(arr,prev+1,len(arr)-1,key)
        
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




class Solution2:
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