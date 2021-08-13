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