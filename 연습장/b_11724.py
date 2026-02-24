import sys
from collections import deque
input = sys.stdin.readline

def bfs(s):
    q = deque()
    q.append(s)
    c[s] = 1
    while q:
        x = q.popleft()
        for nx in g[x]:
            if not c[nx]:
                c[nx] = 1
                q.append(nx)

N, V = map(int, input().split())

g = [[] for _ in range(N+1)]
c = [0]*(N+1)
cnt = 0 

for i in range(V):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)


for i in range(1, N+1):
    if not c[i]:
        cnt += 1
        bfs(i) 


print(cnt)
