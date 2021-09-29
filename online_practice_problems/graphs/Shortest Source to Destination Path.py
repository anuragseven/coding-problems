# Given a 2D binary matrix A(0-based index) of dimensions NxM. Find the minimum number of steps required to reach from (0,0) to (X, Y).
# Note: You can only move left, right, up and down, and only through cells that contain 1.

class Solution:
    def shortestDistance(self,N,M,A,X,Y):
        if A[0][0]==0:
            return -1
        visited=[]
        for i in range(N):
            visited.append([False]*M)
            
        
        result=self.bfs(A,N,M,X,Y,visited)
       
        if result==-1:
            return -1
        
        
        return self.reconstructPath(result,X,Y)
     
    
    
    
    def bfs(self,A,N,M,X,Y,V):
        
        row_q=[0]
        col_q=[0]
        
        V[0][0]=True
        
        dr=[1,-1,0,0]
        dc=[0,0,1,-1]
        
        prev={(0,0):(None,None)}
        
        while row_q!=[]:
            row=row_q.pop(0)
            col=col_q.pop(0)
            
            for i in range(4):
                adjr=row+dr[i]
                adjc=col+dc[i]
                
                
                if 0<=adjr<N and 0<=adjc<M:
                    if A[adjr][adjc]==1 and V[adjr][adjc]==False:
                        V[adjr][adjc]=True
                        
                        row_q.append(adjr)
                        col_q.append(adjc)
                        
                        prev[(adjr,adjc)]=(row,col)
                        
                        if adjr==X and adjc==Y:
                            return prev
        
        
        return -1
        
        
        
    def reconstructPath(self,prev,X,Y):
        
        
        at_x=X
        at_y=Y
        
        path=[]
        
        while at_x!=None and at_y!=None:
            
            path.append([at_x,at_y])
            at_x,at_y=prev[(at_x,at_y)]
       
        return len(path)-1
        
        