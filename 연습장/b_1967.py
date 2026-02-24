import sys
from collections import deque 
input = sys.stdin.readline 

def far_node(s):
    distance = [-1]* (N+1)
    q = deque()
    q.append(s)
    distance[s] = 0 
    
    max_n, max_d = s, 0 
    while q: 
        x = q.popleft()
        for nx, nw in g[x]:
            if distance[nx] == -1:
                q.append(nx)
                distance[nx] = distance[x] + nw
                if max_d < distance[nx]:
                    max_d = distance[nx]
                    max_n = nx
                    
    return (max_n, max_d) 
                
N = int(input())

g = [[] for _ in range(N+1)]

for i in range(N-1):
    a, b, w = map(int, input().split())
    g[a].append((b,w))
    g[b].append((a,w))

far1, _ = far_node(1)
far2, ans = far_node(far1)

print(ans)


