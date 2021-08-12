def bfsOfGraph(V, adj):
        q=[]
        visited=[0]*V
        result=[]
        u=0
        visited[u]=1
        result.append(u)
        q.append(u)
        while q:
            u=q.pop(0)
            for w in adj[u]:
                if visited[w]==0:
                    visited[w]=1
                    q.append(w)
                    result.append(w)
            
        return result