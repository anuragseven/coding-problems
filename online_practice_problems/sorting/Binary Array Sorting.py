# Binary Array Sorting 
def binSort(self, A, N): 
        
        zeroCount=0
        
        for num in A:
            if num==0:
                zeroCount+=1
            
        j=zeroCount
        while zeroCount>0:
            A[zeroCount-1]=0
            zeroCount-=1
        
        while j<N:
            A[j]=1
            j+=1


class Solution:
    
    #Function to sort the binary array.
    def binSort(self, A, N): 
        i=0
        j=N-1
        
        while i<j:
            
            if A[i]==1:
                A[i],A[j]=A[j],A[i]
                j-=1
            else:
                i+=1