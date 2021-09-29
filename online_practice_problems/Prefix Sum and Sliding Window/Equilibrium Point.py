# Given an array A of n positive numbers. The task is to find the first Equilibium Point in the array. 
# Equilibrium Point in an array is a position such that the sum of elements before it is equal to the sum of elements after it.


class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        
        if len(A)==1:
            return 1
        
        l=0
        r=N-1
        s1=0
        s2=0
        s1+=A[l]
        s2+=A[r]
        
        while l<r:
            
            if s1<s2:
                l+=1
                s1+=A[l]
            elif s2<s1:
                r-=1
                s2+=A[r]
                
            else:
                if (l+1)==(r-1):
                    return (l+1)+1
                
                else:
                    l+=1
                    r-=1
                    
                    s1+=A[l]
                    s2+=A[r]
                
            
        return -1
        