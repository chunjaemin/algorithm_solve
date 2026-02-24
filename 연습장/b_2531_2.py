import sys
from collections import defaultdict
input = sys.stdin.readline 

N, d, k, c = map(int, input().split())

nums = []
cnt = defaultdict(int)
for i in range(N):
    nums.append(int(input()))

cnt[c] += 1 
l = 0 
ans = 0 
for r in range(N):
    cnt[nums[r]] += 1 
    if r - l + 1 == k+1:
        cnt[nums[l]] -= 1 
        if cnt[nums[l]] == 0:
            del cnt[nums[l]]
        l += 1  
        ans = max(ans, len(cnt))

print(ans)