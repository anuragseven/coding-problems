# the array A has integers ranging from 1 to N , find the missing integer.
def missingNumber(A, N):
    s1=(N*(N+1))//2
    s2=sum(A)
    return s1-s2

