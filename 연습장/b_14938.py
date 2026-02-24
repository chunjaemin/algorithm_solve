import sys
import heapq 
input = sys.stdin.readline 

#수색범위 M의 제약조건을 가진 체로 탐색, 한번만 찾는게 아닌 여러 경로를 찾아야 하니 
#bfs보단 백트래킹으로 찾으라고 하는 문제 같음 

#아이씨 문제 잘못 이해해서 백트래킹으로 작성함; bfs로 푸는거 같음, 일단 그대로 백트래킹으로 푸는걸로 해야할 듯 
#다익스트라 할 때 dist갱신 잊지말기! 

def dijk(s):
    global max_ans 
    
    ans = 0 
    dist = [sys.maxsize] * (N+1)
    visited_node = [0] * (N+1)
    hq = []
    heapq.heappush(hq, (0,s))
    dist[s] = 0 
    while hq:
        c, x = heapq.heappop(hq)
        
        if c > dist[x]:
            continue 

        if visited_node[x] == 0:
            visited_node[x] = 1
            ans += node_v[x]
        
        for nx, nw in g[x]:
            tc = c + nw  
            if tc < dist[nx] and tc <= M:
                dist[nx] = tc
                heapq.heappush(hq, (tc, nx))

    max_ans = max(max_ans, ans)
    
N, M, R = map(int, input().split())

node_v = [0] + list(map(int, input().split()))
g = [[] for _ in range(N+1)]
max_ans = 0 

for _ in range(R):
    a, b, w = map(int, input().split())
    g[a].append((b, w))
    g[b].append((a, w))

for i in range(1, N+1):
    dijk(i)
print(max_ans)