import sys
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))
nums.sort()

cnt = 0
for i, M in enumerate(nums):
    l, r = 0, len(nums) - 1  
    while l < r:
        if nums[l] + nums[r] == M:
            if l == i:
                l += 1
            elif r == i:
                r -= 1 
            else:  
                cnt += 1 
                break
        elif nums[l] + nums[r] <= M:
            l += 1 
        else:
            r -= 1 

print(cnt)