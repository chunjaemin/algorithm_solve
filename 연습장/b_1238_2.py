import sys
import heapq 
input =sys.stdin.readline 

def dijk(s, g):
    dist = [sys.maxsize] * (N+1)
    hq = []
    
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
ig = [[] for _ in range(N+1)]

for i in range(M):
    a, b, w = map(int, input().split())
    g[a].append((w, b))
    ig[b].append((w, a))


go_party = dijk(X, ig)
go_home = dijk(X, g)
total_party = [0] * (N+1)
for i in range(1, N+1):
    total_party[i] = go_party[i] + go_home[i]
    
print(max(total_party))