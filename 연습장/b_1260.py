import sys
from collections import deque
input = sys.stdin.readline

N, M, V= map(int, input().split())
g = [[] for _ in range(N+1)]
v = [0 for _ in range(N+1)]

for i in range(M):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

for i in range(1, N+1):
    g[i].sort()

def dfs(x):
    v[x] = 1
    print(x, end=" ")
    for nx in g[x]:
        if not v[nx]:
            dfs(nx)

def bfs(s):
    q = deque()
    q.append(s)
    v[s] = 1
    
    while q:
        x = q.popleft()
        print(x, end=" ")
        for nx in g[x]:
            if not v[nx]:
                v[nx] = 1
                q.append(nx)
            
dfs(V)

v = [0 for _ in range(N+1)]
print("")
bfs(V)