#input
import sys
sys.setrecursionlimit(10**6)

M, N, K = map(int, input().split())
coord = []
board = [[0]*N for _ in range(M)] # m, n
area_list = []
for _ in range(K):
    rectangle = [x1, y1, x2, y2] = list(map(int, input().split()))
    coord.append(rectangle)
    for j in range(y1, y2):
        for i in range(x1, x2):
            board[j][i] = -1 # blocked

def adj(pos):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    ret = []
    for x, y in zip(dx, dy):
        try:
            if pos[0]+y >=0 and pos[1]+x >=0 and board[pos[0]+y][pos[1]+x] == 0:
                ret.append((pos[0]+y, pos[1]+x))
        except IndexError:
            pass
    return ret


def dfs(cur, area):
    queue = []
    board[cur[0]][cur[1]] = 1
    queue.append(cur)
    area += 1
    while queue:
        v = queue.pop()
        for adj_node in adj(v):
            if board[adj_node[0]][adj_node[1]] == 0:
                area = dfs(adj_node, area)
    return area

for m in range(M):
    for n in range(N):
        if board[m][n] == 0:
            area_list.append(dfs((m, n), 0))

print(len(area_list))
print(" ".join(map(str, sorted(area_list))))



