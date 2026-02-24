import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * (N + 1)
schedule = []
for i in range(N):
    d, p = map(int, input().split())
    schedule.append((d,p))

for i in range(N-1, -1, -1):
    d, p = schedule[i]
    if i + d - 1 <= N-1:
        dp[i] = max(dp[i+d] + p, dp[i+1])
    else: 
        dp[i] = dp[i+1]
    
print(dp[0])
