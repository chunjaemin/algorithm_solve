import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N, K = map(int, input().split())
g = defaultdict(list)
ans1 = 0 
ans2 = 0 
for i in range(K):
    u, v, w = map(int, input().split())
    g[u].append((v,w))
    g[v].append((u,w))

V1, V2 = map(int, input().split())

def dijkstra(s, g, N):
    INF = sys.maxsize
    dist = [INF]*(N+1)
    dist[s] = 0
    hq = [(0,s)]
    
    while hq:
        c, x = heapq.heappop(hq)
        
        if dist[x] < c:
            continue
        
        for nx, nc in g[x]:
            tc = c + nc 
            if tc < dist[nx]:
                dist[nx] = tc
                heapq.heappush(hq, (tc, nx))
    return dist 

def path_cost(a, b, g, N):
    dist = dijkstra(a,g,N)
    return dist[b]

INF = sys.maxsize
#v1 후 v2
c1 = path_cost(1,V1,g,N)
c2 = path_cost(V1,V2,g,N)
c3 = path_cost(V2,N,g,N)
if c1 != INF and c2 != INF and c3 != INF:
    ans1 = c1 + c2 + c3
else:
    ans1 = INF  
 
c1 = path_cost(1,V2,g,N)
c2 = path_cost(V2,V1,g,N)
c3 = path_cost(V1,N,g,N)
if c1 != INF and c2 != INF and c3 != INF:
    ans2 = c1 + c2 + c3
else:
    ans2 = INF 

if ans1 == INF and ans2 == INF:
    print(-1)
else:
    print(min(ans1, ans2))