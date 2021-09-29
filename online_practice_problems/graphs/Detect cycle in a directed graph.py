# Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.


class Solution:
    
    #Function to detect cycle in a directed graph.
    def isCyclic(self, V, graph):
        
        visited=[False]*V
        dfsVisited=[False]*V
        for v in range(V):
            
            if visited[v]==False:
                
                r=self.dfs(v,dfsVisited,visited,graph)
                if r:
                    return True
    
        return False
    
    def dfs(self,v,dfsVisited,visited,graph):
        
        
        
        visited[v]=True
        dfsVisited[v]=True
        
        for adj in graph[v]:
            
            if visited[adj]==True and dfsVisited[adj]==True:
                return True
            
            elif visited[adj]==False:
                r=self.dfs(adj,dfsVisited,visited,graph)
                if r==True:
                    return True
        
        
        dfsVisited[v]=False
        return False