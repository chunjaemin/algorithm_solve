import sys
input = sys.stdin.readline 

N = int(input())
M = int(input())

nums = list(map(int, input().split()))
nums.sort()
# print(nums)

l, r = 0, len(nums) - 1
cnt = 0 
while l <  r:
    # print(nums[l], nums[r])
    if nums[l] + nums[r] == M:
        r -= 1
        cnt += 1
    elif nums[l] + nums[r]< M:
        l += 1 
    else:  
        r -= 1 

print(cnt)