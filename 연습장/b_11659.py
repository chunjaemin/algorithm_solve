import sys
inpute = sys.stdin.readline 

N, M = map(int, input().split())
nums = list(map(int, input().split()))

dp = [0]* (N+1)
for i in range(1, N+1):
    dp[i] = dp[i-1] + nums[i-1]

for t in range(M):
    s, e = map(int, input().split())
    print(dp[e] - dp[s-1])