import sys
import heapq  
input = sys.stdin.readline 

N, M = map(int, input().split())
S = int(input())
hq = []
dist = [sys.maxsize] * (N + 1)
dist[S] = 0 

g = [[] for _ in range(N+1)]
for i in range(M):
    s, e, v = map(int, input().split())
    g[s].append((v, e))

heapq.heappush(hq,(0,S))

while hq:
    v, e = heapq.heappop(hq)
    if dist[e] < v:
        continue 
    for x in g[e]:
        nv, ne = x 
        tv = v + nv
        if tv < dist[ne]:
            dist[ne] = tv
            heapq.heappush(hq, (tv, ne))

for x in dist[1:]:
    if x == sys.maxsize:
        print("INF")
    else:
        print(x)