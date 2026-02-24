import sys
input = sys.stdin.readline 

N = int(input())

steps = [0]
for i in range(N):
    steps.append(int(input()))

dp = [[0,0] for _ in range(N+1)]
dp[1][0] = steps[1]

if N>=2:
    dp[2][0] = steps[2]
    dp[2][1] = dp[1][0] + steps[2]
for i in range(3, N+1):
    dp[i][0] = max(dp[i-2][0] + steps[i], dp[i-2][1] + steps[i])
    dp[i][1] = dp[i-1][0] + steps[i]

print(max(dp[N]))
