# Brute force
class Solution:
    #Function to count the number of possible triangles.
    def findNumberOfTriangles(self, arr, n):
        result=[]
        
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if self.isTriangle(arr[i],arr[j],arr[k]):
                        result.append([arr[i],arr[j],arr[k]])
                    
        return len(result)       
        
    def isTriangle(self,a,b,c):
        if a+b>c and b+c>a and a+c>b:
            return True
        return False


# Some optimization :

def findNumberOfTriangles(arr, n):
        count=0
        arr.sort()
        
        for i in range(n):
            for j in range(i+1,n):
                k=n-1
                while k>i+1:
                    if arr[i]+arr[j]>arr[k]:
                        count=count+k-j
                        break
                    k-=1
                    
        return count

# more optimization , TC=O(n2)
def findNumberOfTriangles(self, arr, n):
        count=0
        arr.sort()
        
        for i in range(n):
            l=i+1
            r=len(arr)-1
            while l<n:
                if arr[i]+arr[l]>arr[r]:
                    count=count+r-l
                    l+=1
                    r=len(arr)-1
                    
                else:
                    r-=1
            
                    
        return count


# more optimization , from gfg :

def CountTriangles( A):

    n = len(A);

    A.sort(); 

    count = 0;
    
    for i in range(n - 1, 0, -1):
        l = 0;
        r = i - 1;
        while(l < r):
            if(A[l] + A[r] > A[i]):

                # If it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1]..a[r-1], a[r] and a[i]
                count += r - l; 

                # checking for more possible solutions
                r -= 1; 
            
            else:

                # if not possible check for 
                # higher values of arr[l]
                l += 1;