

class Solution:
    def pattern(self, N):
        arr=[]
        try:
            self.getPattern(arr,N,N,False)
        except e:
            print('error')
            
        return arr
    
    def getPattern(self,arr,n,N,f):
        if n==N and f:
            arr.append(N)
            return 
        
        if n>0 and not(f):
            
            arr.append(n)
            n-=5
            self.getPattern(arr,n,N,False)
        
        else:
            
            arr.append(n)
            n+=5
            self.getPattern(arr,n,N,True)