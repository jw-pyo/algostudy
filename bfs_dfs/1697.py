import math
#input
N, K = map(int, input().split())
visited = [0]*100001
ans = 0
def bfs(pos):
    visited[pos] = 1
    ret=[]
    for val in [pos-1, pos+1, 2*pos]:
        if val < 0 or val > 100000: pass
        elif visited[val] == 1: pass
        else: ret.append(val)
    return ret

queue = set([N])
visited[N] = 1
while queue:
    if K in queue: break
    tmp = set()
    for v in queue:
        tmp.update(bfs(v))
    queue = list(tmp)
    ans = ans + 1

print(ans)
