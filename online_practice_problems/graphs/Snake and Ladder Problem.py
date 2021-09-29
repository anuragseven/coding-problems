# Given a 5x6 snakes and ladders board, find the minimum number of dice throws required to reach the destination or last cell (30th cell) from the source (1st cell).

# You are given an integer N denoting the total number of snakes and ladders and an array arr[] of 2*N size where 2*i and (2*i + 1)th values denote the starting and ending point respectively of ith snake or ladder. The board looks like the following.


class Solution:
    def minThrow(self, N, arr):
    
    
        ladders={}
        snakes={}
        for i in range(0,len(arr)-1,2):
            
            if arr[i]>arr[i+1]:
                snakes[arr[i]]=arr[i+1]
            else:
                ladders[arr[i]]=arr[i+1]
       
        position=1
        count=0
        
        visited=[False]*31
        
        prev= self.bfs(ladders,snakes,visited)
        return self.pathReconstruction(prev)
        
        
        
        
    def bfs(self,ladders,snakes,visited):
        
        q=[1]
        prev=[None]*31
        visited[1]=True
        while q!=[]:
            pos=q.pop(0)
            for i in range(1,7):
                
                if visited[pos+i]==False:
                    if pos+i in ladders:
                        q.append(ladders[pos+i])
                        visited[pos+i]=True
                        visited[ladders[pos+i]]=True
                        
                        prev[ladders[pos+i]]=pos
                        
                        if ladders[pos+i]==30:
                            return prev
                    
                    elif pos+i not in snakes:
                        q.append(pos+i)
                    
                        visited[pos+i]=True
                    
                        prev[pos+i]=pos
                        
                        if pos+i==30:
                            return prev
                    
                
    def pathReconstruction(self,prev):
        
        at=30
        path=[]
        
        while at!=None:
            
            path.append(at)
            at=prev[at]
        
        return len(path)-1