import sys
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))
nums.sort()
# print(nums)
cnt = 0 
for i, x in enumerate(nums): 
    l, r = i+1, N-1
    while l<r:
        if l == i:
            l += 1 
        elif r == i:
            r -= 1
        elif nums[l] + nums[r] < -x:
            l += 1 
        elif nums[l] + nums[r] > -x:
            r -= 1
        elif nums[l] + nums[r] == -x:
            # print("l:",l, "nums[l]:",nums[l], "r:",r, "nums[r]:",nums[r], "x:", x)
            if nums[l] == nums[r]:
                n = r - l + 1 
                cnt += n*(n-1) // 2 
                break 
            else:
                l_cnt = 1 
                r_cnt = 1
                # print(nums[l], nums[r], end=" ") 
                while l + 1 < r and nums[l] == nums[l+1]:
                    l_cnt += 1
                    l += 1 
                while l < r - 1 and nums[r] == nums[r-1]:
                    r_cnt += 1 
                    r -= 1 
                l += 1
                r -= 1 
                cnt += l_cnt * r_cnt
                # print(l_cnt * r_cnt)

print(cnt)