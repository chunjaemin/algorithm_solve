import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
V = int(input())

g = [[] for _ in range(N+1)]
c = [0 for _ in range(N+1)]

for i in range(V):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

# print(g[1])

def dfs(x):
    for nx in g[x]:
        if c[nx] == 0:
            c[nx] = 1
            dfs(nx)

def bfs (s):
    q = deque()
    q.append(s)
    c[s] = 1
    while q:
        x = q.popleft()
        for nx in g[x]:
            if not c[nx]:
                c[nx] = 1 
                q.append(nx)
            

bfs(1)
print(sum(c) - 1)