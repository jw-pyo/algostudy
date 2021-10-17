from collections import deque
F, S, G, U, D = map(int, input().split())
visited = [0]*(F+1)

def adj(pos):
    dp = [U, -1*D]
    ret = []
    for p in dp:
        if 0 < pos + p <= F and visited[pos+p] == 0:
            ret.append(pos+p)
    return ret

def bfs(start):
    depth = 0
    queue = deque([(start, depth)])
    visited[start] = 1
    while queue:
        v = queue.popleft()
        if v[0] == G: return v[1]
        for adj_node in adj(v[0]):
            if visited[adj_node] == 0:
                queue.append((adj_node, v[1]+1))
                visited[adj_node] = 1        
    return "use the stairs"

print(bfs(S))
