import sys
input = sys.stdin.readline

N, K = map(int, input().split())

nums = list(map(int, input().split()))
  
n_sum = sum(nums[0:K])
ans = n_sum
for i in range(1, N - K+1):
    n_sum = n_sum - nums[i-1] + nums[i + K - 1]
    ans = max(ans, n_sum)

print(ans)