import sys
input = sys.stdin.readline 

def check(x):
    r = 0 
    for i in range(len(nums)):
        r += max(0, nums[i] - x)
    return r

N, M = map(int, input().split())

nums = list(map(int, input().split()))


l, r = 0, max(nums)
ans = 0
while l <= r:
    m = (l + r) // 2
    chk = check(m)
    if chk > M:
        l = m + 1
        ans = max(ans, m) 
    elif chk < M:
        r = m - 1
    else:
        ans = max(ans, m)
        break
print(ans)
        