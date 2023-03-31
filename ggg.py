graph = {'A': ['C', 'B'],
    'B': ['D', 'A', 'C'],
    'C': ['F', 'A'],
    'D': ['B'],
    'E': ['F', 'B'],
    'F': ['C', 'E']}

visited = []
Q = []
BFS = []

def bfs(v):
    if v in visited:
        return
    visited.append(v)
    BFS.append(v)

    for i in graph:
        if not i in visited:
            Q.append(i)
    while Q:
        bfs(Q.pop(0))

start = 'A'
bfs(start)
print(BFS)