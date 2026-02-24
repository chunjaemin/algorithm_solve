import sys
input = sys.stdin.readline 

N, M = map(int ,input().split())
nums = list(map(int, input().split()))
cnt = 0 

r = 0
n_sum = nums[0]
for i in range(N):
    while n_sum < M and r<N:
        n_sum += nums[r] 
        r += 1
    if n_sum == M:
        cnt += 1
    n_sum -= nums[i]

print(cnt)