import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

nums = [] 
for i in range(N):
    nums.append(int(input()))

# print(nums)

nums.sort()
ans = sys.maxsize
l = 0 

for r in range(N):
    while nums[r] - nums[l] >= M and l < r:
        ans = min(ans, nums[r] - nums[l])
        l += 1  

print(ans)