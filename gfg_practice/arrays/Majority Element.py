# TC=O(n), SC=O(n)
def majorityElement(self, A, N):
        
        n=(N//2)+1
        
        counts={}
        for val in A:
            if val in counts:
                counts[val]+=1
            else:
                counts[val]=1
                
        for num in counts:
            if counts[num]>=n:
                return num
        
        return -1

# TC=O(n), SC=O(1)
def majorityElement(self, A, N):
    
        
        maj_index=0
        count=0
        n=(len(A)//2)+1
        
        for i in range(len(A)):
            if A[i]==A[maj_index]:
                count+=1
            else:
                count-=1
                
            if count==0:
                maj_index=i
                count=1
                
            if count >=n:
                return A[maj_index]
        count=0
        for val in A:
            if val==A[maj_index]:
                count+=1
        
        return A[maj_index] if count>=n else -1