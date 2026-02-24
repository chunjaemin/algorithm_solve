import sys
import heapq 
input = sys.stdin.readline 

N, E = map(int, input().split())
g = [[] for _ in range(N+1)] 

for i in range(E):
    s, e, v = map(int, input().split())
    g[s].append((v,e))
    g[e].append((v,s))

S1, S2 = map(int, input().split())

def dijkstra(s, e):
    hq = [] 
    heapq.heappush(hq, (0, s))
    dist = [sys.maxsize] * (N+1)
    dist[s] = 0 
    
    while hq:
        cc, ce = heapq.heappop(hq)
        if dist[ce] < cc:
            continue
        for nv, ne in g[ce]:
            tc = cc + nv
            if tc < dist[ne]:
                dist[ne] = tc
                heapq.heappush(hq, (tc, ne))
    return dist[e]

path1 = dijkstra(1,S1)
path2 = dijkstra(S1, S2)
path3 = dijkstra(S2, N)

path4 = dijkstra(1,S2)
path5 = dijkstra(S2, S1)
path6 = dijkstra(S1, N)

if path1 != sys.maxsize and path2 != sys.maxsize and path3 != sys.maxsize:
    ans1 = path1 + path2 + path3
else:
    ans1 = sys.maxsize

if path4 != sys.maxsize and path5 != sys.maxsize and path6 != sys.maxsize:
    ans2 = path4 + path5 + path6
else:
    ans2 = sys.maxsize

result = min(ans1, ans2)
if result == sys.maxsize:
    print(-1)
else:
    print(result)