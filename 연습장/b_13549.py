# 3가지경우 모두 실행되어야 하는데 중간에 continue때문에 일부 실행이 스킵되서 정답 안나왔었음 
import sys
import heapq 
input = sys.stdin.readline 

S, E = map(int, input().split())

N = 100000
visited = [sys.maxsize] * (N+1)

hq = [] 
heapq.heappush(hq,(0,S))
visited[S] = 0 
while hq:
    v, n = heapq.heappop(hq)
    if n == E:
        print(v)
        exit()
    
    if v > visited[n]:
        continue
    
    if 2*n <= N:
        if visited[n*2] > v:
            visited[n*2] = v
            heapq.heappush(hq, (v, n*2))

    
    if n+1 <= N:
        if visited[n+1] > v + 1:
            visited[n+1] = v + 1
            heapq.heappush(hq, (v + 1, n+1))
    
    if n-1 >= 0:
        if visited[n-1] > v + 1:
            visited[n-1] = v + 1
            heapq.heappush(hq, (v + 1, n-1))

