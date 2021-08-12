# create a graph using adjacency list
g = {
    1: [2, 3],
    2: [1, 4, 5],
    3: [1, 6, 7],
    4: [2, 8],
    5: [2, 8],
    6: [3, 8],
    7: [3, 8],
    8: [4, 5, 6, 7]
}
g1 = {
    1: [2, 3],
    2: [1, 4],
    3: [1, 4],
    4: [2, 3],
    5: [6, 7],
    6: [5, 7],
    7: [6, 5]
}


# write code for breadth first search
def bFS(g, v, visited):
    u = v
    visited[v] = 1
    print(v)

    q = []
    while True:
        for vertice in g[u]:
            if visited[vertice] == 0:
                q.append(vertice)
                visited[vertice] = 1
                print(vertice)
        if len(q) == 0:
            return
        u = q.pop(0)


def bFT(g, visited):
    for vetex in visited:
        if visited[vetex] == 0:
            bFS(g, vetex, visited)


def dFS(g, v, visited):
    visited[v] = 1
    print(v)
    for vertex in g[v]:
        if visited[vertex] == 0:
            dFS(g, vertex, visited)


def dFT(g, visited):
    for vertex in visited:
        if visited[vertex] == 0:
            dFS(g, vertex, visited)


visited = {i: 0 for i in range(8)}
g3 = {0: [2, 4, 5],
      1: [2, 4, 5],
      2: [6],
      3: [5, 7],
      4: [6, 7],
      5: [7],
      6: [],
      7: []}
bFS(g3, 0, visited)
