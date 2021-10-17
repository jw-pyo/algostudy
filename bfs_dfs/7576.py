from collections import deque
#input 

m, n = map(int, input().split())
tomatoes = []
checked = [[0]*m for _ in range(n)]
get_indices = []
for _ in range(n):
    tomatoes.append(list(map(int, input().split())))
for y in range(n):
    for x in range(m):
        if tomatoes[y][x] == 1:
            get_indices.append((y, x))

def isAdj(pos1, pos2):
    if pos2[0] == -1 or pos2[0] == n or pos2[1] == -1 or pos2[1] == m:
        return False
    elif tomatoes[pos2[0]][pos2[1]] == 0:
        if checked[pos2[0]][pos2[1]] == 0:
            return True
        else:
            return False
    return False

def adj(pos):
    up, down, left, right = (pos[0]-1, pos[1]), (pos[0]+1, pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1)
    ret = []
    if isAdj(pos, left):
        ret.append(left)
    if isAdj(pos, right):
        ret.append(right)
    if isAdj(pos, up):
        ret.append(up)
    if isAdj(pos, down):
        ret.append(down)
    return ret

def bfs(pos):
    queue = deque()
    queue.append(pos)
    checked[pos[0]][pos[1]] = 1
    ret = adj(pos)
    for adj_node in ret:
        tomatoes[adj_node[0]][adj_node[1]] = 1
    return ret

day = 0
while get_indices:
    ret = []
    for start_pos in get_indices:
        ret.extend(bfs(start_pos))
    ret = list(set(ret))
    get_indices = ret
    day += 1

if any(0 in sl for sl in tomatoes): print(-1)
else: print(day-1)












