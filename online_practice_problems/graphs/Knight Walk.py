'''
Given a square chessboard, the initial position of Knight and position of a target. Find out the minimum steps a Knight will take to reach the target position.
Note:
The initial and the target position co-ordinates of Knight have been given accoring to 1-base indexing.
'''



class Solution:
	def minStepToReachTarget(self, knightPos, targetPos, N):
	    if N==1:
	        return 0
	    visited=[]
	    
	    for i in range(N):
	        visited.append([False]*N)
	    
	    
	    sr=knightPos[0]-1
	    sc=knightPos[1]-1
	    
	    tr=targetPos[0]-1
	    tc=targetPos[1]-1
	    
	    prev=self.bfs(sr,sc,tr,tc,visited) 
	    if prev==None:
	        return -1
	    return self.reconstructPath(prev, tr,tc)    
	def bfs(self,sr,sc,tr,tc,visited):
	    
	    dx=[1,1,-1,-1,2,-2,2,-2]
	    dy=[2,-2,2,-2,1,1,-1,-1]
	    
	    visited[sr][sc]=True
	    
	    row_q=[sr]
	    col_q=[sc]
	    
	    prev={(sr,sc):(None,None)}
	    
	    while row_q!=[]:
	        
	        row=row_q.pop(0)
	        col=col_q.pop(0)
	        
	        for i in range(8):
	            adjr=row+dx[i]
	            adjc=col+dy[i]
	            
	            
	            if 0<=adjr<N and 0<=adjc<N:
	                
	                if visited[adjr][adjc]==False:
	                    visited[adjr][adjc]=True
	                    row_q.append(adjr)
	                    col_q.append(adjc)
	                    
	                    
	                    prev[(adjr,adjc)]=(row,col)
	                    
	                    if adjr==tr and adjc==tc:
	                        return prev
	                    
	  
	  
    def reconstructPath(self,prev,tr,tc):
	      
        path=[]
	             
	    at_x=tr
	    at_y=tc
	      
	    while at_x!=None and at_y!=None:
	        path.append([at_x,at_y])
	        at_x,at_y=prev[(at_x,at_y)]
	                   
	    return len(path)-1              
	                    