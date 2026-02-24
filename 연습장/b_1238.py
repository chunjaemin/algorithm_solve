import sys
import heapq 
input = sys.stdin.readline 

def dijk(s):
    hq = []
    dist = [sys.maxsize] * (N+1)
    
    heapq.heappush(hq, (0, s))
    dist[s] = 0 
    
    while hq:
        c, x = heapq.heappop(hq)
        if dist[x] < c:
            continue
        
        for w, nx in g[x]:
            tc = c + w 
            if tc < dist[nx]:
                dist[nx] = tc
                heapq.heappush(hq, (tc, nx))
    return dist

N, M, X = map(int, input().split())

g = [[] for _ in range(N+1)]

for i in range(M): 
    a, b, w = map(int, input().split())
    g[a].append((w, b))

go_party = [sys.maxsize] * (N+1)
back_home = dijk(X)
total_dist = [0] * (N+1)

for x in range(1,N+1):
    dijk_dist = dijk(x)
    go_party[x] = dijk_dist[X]
    total_dist[x] = go_party[x] + back_home[x]

print(max(total_dist))

# print(dijk(1))
# print(g)

