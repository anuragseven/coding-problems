from math import ceil
def connectedSum(graph_nodes, graph_from, graph_to):
    print(graph_nodes)
    g={}
    for i in range(len(graph_from)):
        if graph_from[i]  in g:
            
            g[graph_from[i]].append(graph_to[i])
        else:
        
            g[graph_from[i]]=[]
            g[graph_from[i]].append(graph_to[i])
        
    print(g)
    visited=[0]*(graph_nodes+1)
    result=0
    nodeCount=0
    for key in g.keys():
        if visited[key]==0:
            setCount=bfs(g,key,visited)
            print(setCount)
            nodeCount+=setCount
            result+=ceil(setCount**0.5)
    print(nodeCount)
    if graph_nodes-nodeCount!=0:
        result+=graph_nodes-nodeCount
    return result
def bfs(g,v,visited):
    count=1
    visited[v]=1
    q=[]
    
    q.append(v)
    while q:
        u=q.pop()
        if u in g:
            for w in g[u]:
                if visited[w]==0:
                    visited[w]=1
                    count+=1
                    q.append(w)
    return count    