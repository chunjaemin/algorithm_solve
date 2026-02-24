import sys
input = sys.stdin.readline

N, S = map(int, input().split())
nums = list(map(int, input().split()))

l = 0
sum_val = 0 
ans = sys.maxsize
for r in range(N):
    sum_val += nums[r]
    if sum_val >= S:
        while sum_val >= S:
            ans = min(r - l + 1, ans)
            sum_val -= nums[l]
            l += 1
    
if ans == sys.maxsize:
    ans = 0
print(ans)