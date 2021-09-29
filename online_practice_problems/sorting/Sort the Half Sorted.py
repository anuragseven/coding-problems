# Given an integer array of which both first half and second half are sorted. The task is to merge two sorted halves of the array into a single sorted array.
# Note: The two halves can be of arbitrary sizes.

class Solution:
    def sortHalves (self, A, n):
        
        prev=float('-inf')
        index=-1
        for i in range(n):
            if arr[i]<prev:
                index=i
                break
            else:
                prev=arr[i]
        if index==-1:
            return
        self.merge(A,0,index-1,len(A)-1)
                
        
        
    def merge(self,arr,p,q,r):
        
        L=[]
        R=[]
        
        for i in range(p,q+1):
            L.append(arr[i])
            
        for i in range(q+1,r+1):
            R.append(arr[i])
 
        L.append(float('inf'))
        R.append(float('inf'))
        
        i=0
        j=0
        for k in range(p,r+1):
            if L[i]<=R[j]:
                arr[k]=L[i]
                i+=1
            else:
                arr[k]=R[j]
                j+=1