# Given an adjacency list of a graph adj  of V no. of vertices having 0 based index. Check whether the graph is bipartite or not.

class Solution:
	def isBipartite(self, V, graph):
	
	    colored=[-1]*V
	    
	    for v in range(V):
	        
	        if colored[v]==-1:
	            r=self.bfs(v,graph,colored)
	            if r==False:
	                return False
	    
	    return True
	    
	    
	    
    def bfs(self,v,graph,colored):
        
        q=[v]
        colored[v]=1
        
        while q!=[]:
            u=q.pop(0)
            for adj in graph[u]:
                if colored[adj]==-1:
                    if colored[u]==1:
                        colored[adj]=0
                    else:
                        colored[adj]=1
                    q.append(adj)
                
                elif colored[u]==colored[adj]:
                    return False
        
        return True
	