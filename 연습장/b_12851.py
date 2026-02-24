import sys
from collections import deque 
input = sys.stdin.readline

#BFS로 최단시간 찾는건 문제가 안됨
#중복 정답이 되는 모든 케이스를 저장? 가능한가? 
#visited는 한번만 기록이 될 것임 이러면 bfs가 아니라 백트래킹을 통해 해야하나? 3^n이라 될 수가 없음 
#bfs로 해야하는데 how??

#bfs가 안된다고 하면 DP인가? 
#DP[n] = 최단시간으로 n에 도달했을 때의 경우의 수? 
#dp테이블 채우는게 말이 안됨 어디서부터 채울지 너무 불명확함  

N, K  = map(int, input().split())

visited = [-1] * 100001
q = deque()
q.append(N)
visited[N] = 0

cnt = 0 
finish = 0 
ans = 0 
while q:    
    for i in range(len(q)):
        x = q.popleft()
        
        if x == K:
            cnt += 1 
            ans = visited[x]
            finish = 1 
        
        for nx in (x+1, x-1, 2*x):
            if 0<= nx <= 100000:
                if visited[nx] == -1 or visited[nx] == visited[x] + 1:
                    q.append(nx)
                    visited[nx] = visited[x] + 1
    if finish == 1:
        break 

print(ans)
print(cnt)