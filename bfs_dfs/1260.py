from collections import deque

# input
N,M,V= map(int, input().split())
graph = dict()
for _ in range(M):
    v1, v2 = map(int, input().split())
    if v1 not in graph: graph[v1] = [v2]
    else: graph[v1].append(v2)

    if v2 not in graph: graph[v2] = [v1]
    else: graph[v2].append(v1)
for key in graph.keys():
    graph[key].sort()
# solution
visited_dfs = []
visited_bfs = []

def dfs(node, graph):
    visited_dfs.append(node)
    if node in graph:
        for next_node in graph[node]:
            if next_node not in visited_dfs:
                dfs(next_node, graph)

def bfs(node, graph):
    queue = deque()
    queue.append(node)
    visited_bfs.append(node)
    while queue:
        v = queue.popleft()
        if v in graph:
            for next_node in graph[v]:
                if next_node not in visited_bfs:
                    queue.append(next_node)
                    visited_bfs.append(next_node)
dfs(V, graph)
bfs(V, graph)
print(" ".join(map(str, visited_dfs)))
print(" ".join(map(str, visited_bfs)))


