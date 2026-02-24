import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
S = int(input())
g = [[] for _ in range(V+1)]

for _ in range(E):
    u,v,w = map(int, input().split())
    g[u].append((v,w))

def dijkstra(s,g,v):
    INF = sys.maxsize
    dist = [INF]* (v+1)
    dist[s] = 0
    hq = [(0,s)]
    
    while hq:
       c, x = heapq.heappop(hq)
       
       if (dist[x] < c):
           continue
       
       for nx, nc in g[x]:
           tc = c + nc
           if (tc < dist[nx]):
               dist[nx] = tc
               heapq.heappush(hq, (tc, nx))
    return dist
dist = dijkstra(S, g, V)

for i in range(1, V+1):
    if dist[i] == sys.maxsize:
        print("INF")
    else: 
        print(dist[i])