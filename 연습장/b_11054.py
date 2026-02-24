import sys
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input())

nums = list(map(int, input().split()))
dp = [1] * N
r_dp = [1] * N 

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(i, N):
        if nums[i] > nums[j]:
            r_dp[i] = max(r_dp[i], r_dp[j] + 1)

ans = 0         
for i in range(N):
    ans = max(ans, dp[i]+r_dp[i]-1)

print(ans)