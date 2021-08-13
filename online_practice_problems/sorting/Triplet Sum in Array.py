# Given an array arr of size n and an integer X. Find if there's a triplet in the array which sums up to the given integer X.


def find3Numbers(A, X):
        A.sort()
        
    
        for i in range(len(A)-1):
            l=i+1
            r=len(A)-1
            while l<r:
                if A[i]+A[l]+A[r]==X:
                    return True
                elif A[i]+A[l]+A[r]<X:
                    l+=1
                    
                elif A[i]+A[l]+A[r]>X:
                    r-=1
        return False