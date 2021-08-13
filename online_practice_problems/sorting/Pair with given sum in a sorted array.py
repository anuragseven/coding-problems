#You are given an array Arr of size N. You need to find all pairs in the array that sum to a number K. If no such pair exists then output will be -1. The elements of the array are distinct and are in sorted order.
#Note: (a,b) and (b,a) are considered same. Also, an element cannot pair with itself, i.e., (a,a) is invalid.


def Countpair (self, arr, n, sum) : 
        l=0
        r=n-1
        count=0
        while l<r:
            if arr[l]+arr[r]==sum :
                count+=1
                l+=1
                r-=1
            
            elif arr[l]+arr[r]<sum:
                l+=1
            
            else:
                r-=1
        return count if count!=0 else -1 