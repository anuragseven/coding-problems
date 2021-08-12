# Square root of a number or floor of sqrt of x

class Solution:
    def floorSqrt(self, x): 
        return self.search(x)
    
    def search(self,x):
        start=0
        end=x
        ans=-1
        while start<=end:
            mid=(start+end)//2
            if mid*mid==x :
                return mid
            elif mid*mid>x:
                end=mid-1
            else:
                
                start=mid+1
                ans=mid
            
        return ans