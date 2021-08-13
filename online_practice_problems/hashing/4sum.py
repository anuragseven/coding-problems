# https://cs.stackexchange.com/questions/2973/generalised-3sum-k-sum-problem
# 4 sum problem , need to be optimised
class Solution:
    def fourSum(self, A, k):
        A.sort()
        n=len(A)
        result=[]
        for i in range(n - 3):
            for j in range(i + 1, n - 2):
             
            # Initialize two variables as indexes
            # of the first and last elements in
            # the remaining elements
                l = j + 1
                r = n - 1
 
            # To find the remaining two elements,
            # move the index variables (l & r)
            # toward each other.
                while (l < r):
                    if(A[i] + A[j] + A[l] + A[r] == k):
                        result.append([A[i] , A[j] , A[l] , A[r]])
                        l += 1
                        r -= 1
                 
                    elif (A[i] + A[j] + A[l] + A[r] < k):
                        l += 1
                    else: # A[i] + A[j] + A[l] + A[r] > k
                        r -= 1
        
        finalResult=[]
        for  i in result:
            continueFlag=False
            for j in finalResult:
                if i==j:
                    continueFlag=True
                    break
            if not(continueFlag):
                finalResult.append(i)
    
        return finalResult