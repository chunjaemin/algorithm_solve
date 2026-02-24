import sys
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))

l, r = 0, N - 1 
ans = sys.maxsize
ans_l = -1
ans_r = -1
while l < r: 
    if abs(ans) > abs(nums[l] + nums[r]):
        ans = nums[l] + nums[r]
        ans_l = l 
        ans_r = r 
    if nums[l] + nums[r] > 0:
        r -= 1
    else: 
        l += 1  

print(nums[ans_l], nums[ans_r])