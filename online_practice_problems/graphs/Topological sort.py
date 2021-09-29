# Given a Directed Acyclic Graph (DAG) with V vertices and E edges, Find any Topological Sorting of that Graph.

class Solution:
    
    #Function to return list containing vertices in Topological order.
    def topoSort(self, V, graph):
        visited=[False]*V
        ordering=[-1]*V
        i=V-1
        for v in range(V):
            
            if visited[v]==False:
                
                i=self.dfs(v,i,ordering,visited,graph)
        
        
        return ordering
        
        
    def dfs(self,v,i,ordering,visited,graph):
        
        visited[v]=True
        
        for adj in graph[v]:
            if visited[adj]==False:
            
                i=self.dfs(adj,i,ordering,visited,graph)
            
        
        ordering[i]=v
        i-=1
        return i