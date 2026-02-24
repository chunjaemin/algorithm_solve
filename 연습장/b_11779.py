import sys
import heapq 
input =sys.stdin.readline 

#다익스트라 + 경로복원 문제인듯 

def dijk(s, e):
    dist = [sys.maxsize] * (N+1)
    hq = []
    heapq.heappush(hq, (0, s))
    dist[s] = 0
    
    parent = [x for x in range(N+1)]
    
    while hq:
        c, x = heapq.heappop(hq)
        
        if dist[x] < c:
            continue 
        
        for nw, nx in g[x]:
            tc = c + nw
            if tc < dist[nx]:
                dist[nx] = tc
                heapq.heappush(hq, (tc, nx))
                parent[nx] = x 
    
    path = []
    cur = e 
    while cur != s:
        path.append(cur)
        cur = parent[cur]
    path.append(s)
    
    return [dist[e], len(path), path[::-1]]  


N = int(input())
M = int(input())

g = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    g[a].append((w, b))

S, E = map(int, input().split())

# print(g)
ans1, ans2, ans_path = dijk(S,E)

print(ans1)
print(ans2)
print(" ".join(map(str, ans_path)))