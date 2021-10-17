T = int(input())
ret = []
for _ in range(T):
    width = int(input())
    cur = tuple(map(int, input().split()))
    after = tuple(map(int, input().split()))
    
    visited = [[0]*width for _ in range(width)]
    queue = list()
    queue.append(cur)
    visited[cur[0]][cur[1]] = 1
    depth = 0
    
    def adj(pos: tuple()):
        knight_pos = [(1,2), (2,1), (-1,2), (2,-1),(1,-2),(-2,1),(-1,-2),(-2,-1)]
        knight_pos = [(pos[0]+v[0], pos[1]+v[1]) for v in knight_pos]
        ret = []
        for i, loc in enumerate(knight_pos):
            if loc[0] < 0 or loc[0] >= width or loc[1] < 0 or loc[1] >= width:
                pass
            elif visited[loc[0]][loc[1]] == 1:
                pass
            else: 
                ret.append(loc)
        return ret
    def bfs(pos: tuple()):
        visited[pos[0]][pos[1]] = 1
        return adj(pos) 
    
    while queue:
        next_queue =list()
        for next_pos in queue:
            adj_list = bfs(next_pos)
            next_queue.extend(adj_list)
        next_queue = list(set(next_queue))
        queue = next_queue
        if visited[after[0]][after[1]] == 1: break
        depth += 1
    ret.append(depth)

for r in ret:
    print(r)
