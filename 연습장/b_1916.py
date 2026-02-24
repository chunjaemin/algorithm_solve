import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
K = int(input())

g= defaultdict(list)
for i in range(K):
    u, v, w = map(int, input().split())
    g[u].append((v,w))
S, E = map(int, input().split())


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
dist = dijkstra(S,g,N)

print(dist[E])




    