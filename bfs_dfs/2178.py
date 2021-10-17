n,m = map(int, input().split())
maze = []
visited = [[0]*m]*n
for i in range(n):
    maze.append(list(map(int, list(input()))))

def adj_list(node_pos):
    y, x = node_pos
    cand_ret = [(y-1, x), (y+1, x), (y, x-1), (y,x+1)]
    if x == 0 and y == 0: cand_ret = [(0,1), (1,0)]
    elif x == 0 and y != 0: cand_ret = [(y-1, 0), (y+1, 0), (y,1)]
    elif x != 0 and y == 0: cand_ret = [(1, x), (0, x-1), (0, x+1)] 
    ret = []
    for adj in cand_ret:
        try:
            value, visit = maze[adj[0]][adj[1]], visited[adj[0]][adj[1]]
            if value == 1 and visit == 0:
                ret.append(adj)
        except IndexError:
            pass
    return ret

def dfs(pos, maze, prev_depth):
    visited[pos[0]][pos[1]] = 1
    # print(adj_list(pos))
    if pos[0] == n-1 and pos[1] == m-1:
        print(prev_depth)
        return
    if len(adj_list(pos)) > 0:
        for next_pos in adj_list(pos):
            if visited[next_pos[0]][next_pos[1]] == 0:
                dfs(next_pos, maze, prev_depth+1)

dfs((0,0), maze, 0)

