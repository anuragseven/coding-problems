# Given two strings A and B, find if A is a subsequence of B.
def isSubSequence( A, B):
        
        i=0
        j=0
        
        while i<len(A) and j<len(B):
            
            if A[i]==B[j]:
                i+=1
                j+=1
                
            else:
                j+=1
            
        
        if i==len(A):
            return True
        
        return False

