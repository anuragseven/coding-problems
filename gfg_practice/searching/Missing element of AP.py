# Find the missing element from an ordered array arr[], consisting of N elements representing an Arithmetic Progression(AP).

def findMissing(self, arr, n):
        if len(arr)==2:
            return (arr[0]+arr[1])//2
        
        d1=arr[1]-arr[0]
        d2=arr[-1]-arr[-2]
        d=min(d1,d2)
        
        s1=((n+1)*(2*arr[0]+n*d))//2
        s2=sum(arr)
        return s1-s2



class Solution:
    def findMissing(self, arr, n):
        if len(arr)==2:
            return (arr[0]+arr[1])//2
        d1=arr[1]-arr[0]
        d2=arr[-1]-arr[-2]
        d=min(d1,d2)
        return self.search(arr,d,0,len(arr)-1)
    def search(self,arr,d,l,h):
        if h<=l:
            return 
        mid=l+(h-l)//2
        
        if arr[mid]+d!=arr[mid+1]:
            return arr[mid]+d
        if mid>0 and arr[mid-1]+d!=arr[mid]:
            return arr[mid-1]+d
        
        if arr[mid]==arr[0]+mid*d:
            return self.search(arr,d,mid+1,h)
        
        else:
            return self.search(arr,d,l,mid-1)