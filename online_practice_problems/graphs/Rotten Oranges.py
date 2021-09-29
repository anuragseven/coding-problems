'''
Given a grid of dimension nxm where each cell in the grid can have values 0, 1 or 2 which has the following meaning:
0 : Empty cell
1 : Cells have fresh oranges
2 : Cells have rotten oranges

We have to determine what is the minimum time required to rot all oranges. A rotten orange at index [i,j] can rot other fresh orange at indexes [i-1,j], [i+1,j], [i,j-1], [i,j+1] (up, down, left and right) in unit time. 

'''


from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		R=len(grid)
		C=len(grid[0])
	
		row_q=deque()
	    col_q=deque()
		totalOrange=0
		for i in range(R):
		    for j in range(C):
		        if grid[i][j]==1 or grid[i][j]==2:
		        
		            if grid[i][j]==2:
		                row_q.append(i)
		                col_q.append(j)
		            totalOrange+=1
		 
	    time,totalOrangeRotted=self.bfs(row_q,col_q,grid,R,C)
		 
	    return time if totalOrangeRotted==totalOrange else -1
		            
		
		
		
		
	def bfs(self,row_q,col_q,grid,R,C):
	    dx=[1,-1,0,0]
	    dy=[0,0,1,-1]
	  
	    
	  
	    
	    count=0
	    time=0
	    totalOrangeRotted=0
	    
	    while len(row_q)!=0:
	        count=len(row_q)
	        totalOrangeRotted+=count
	        
	        while count!=0:
	            row=row_q.popleft()
	            col=col_q.popleft()
	            
	            for i in range(4):
	                adjr=row+dx[i]
	                adjc=col+dy[i]
	                
	                if 0<=adjr<R and 0<=adjc<C:
	                    if grid[adjr][adjc]==1:
	                         grid[adjr][adjc]=2
	                         row_q.append(adjr)
	                         col_q.append(adjc)
	            count-=1
	                         
            if len(row_q)!=0:
	            time+=1
        return time,totalOrangeRotted