import sys
from collections import deque
input = sys.stdin.readline 

N = int(input())
g = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

visited = [0]*(N+1)
parent = [-1]*(N+1)
q = deque()
q.append(1)
while q:
    cur = q.popleft()
    for x in g[cur]:
        if visited[x] == 0:
            visited[x] = 1
            parent[x] = cur
            q.append(x)

for i in range(2,N+1):
    print(parent[i])

