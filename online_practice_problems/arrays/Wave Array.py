#Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it. In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5..... (considering the increasing lexicographical order).
def convertToWave(self,A,N):
        for i in range(0,len(A),2):
            if i+1==len(A):
                return A
            
            A[i],A[i+1]=A[i+1],A[i]
        return A