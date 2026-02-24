import sys
from collections import deque 
input = sys.stdin.readline 


C, N = map(int, input().split())
dp = [sys.maxsize] * (C+1) # dp[i] = i만큼의 인원수를 채웠을 때 최소 금액 

ops = []
for _ in range(N):
    p, v = map(int, input().split())
    ops.append((p, v))

dp[0] = 0 
q = deque()
q.append(0)
ans = sys.maxsize 
while q:
    v = q.popleft()
    
    for ec, ev in ops:
        # print(ec, ev)
        nc, nv = dp[v] + ec, v + ev
        if nv < C:
            if dp[nv] > nc:
                dp[nv] = nc 
                q.append(nv)
        else:
            ans = min(ans, nc)
# print(dp)
print(ans)
