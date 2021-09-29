# Given an undirected graph with V vertices and E edges, check whether it contains any cycle or not. 


class Solution:
    
    #Function to detect cycle in an undirected graph.
    def isCycle(self, V, graph):
		
        visited=[False]*V
	    
		
	for v in range(V):
		    
	    if visited[v]==False:
		        
		        
	        r=self.dfs(v,-1,visited,graph)
                if r:
                    return True
        
        return False
        
        
    def dfs(self,v,prev,visited,graph):
        
        visited[v]=True
        
        for adj in graph[v]:
            if visited[adj]==True and prev!=adj:
                return True
            elif visited[adj]==False:
                r=self.dfs(adj,v,visited,graph)
                
                if r:
                    return True
        
        return False