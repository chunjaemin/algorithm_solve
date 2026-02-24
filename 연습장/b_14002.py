import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

dp = [1]*N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i],dp[j]+1)

ans_dp = max(dp)
print(ans_dp)

result = []
target_len = ans_dp
prev_num = sys.maxsize 
for i in range(N-1, -1, -1):
    if dp[i] == target_len and nums[i] < prev_num:
        prev_num = nums[i]
        result.append(nums[i])
        target_len -= 1 

print(" ".join(map(str, result[::-1])))