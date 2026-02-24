import sys
from collections import defaultdict
input = sys.stdin.readline 

N, d, k, c = map(int, input().split())

nums = []
for i in range(N):
    nums.append(int(input()))
    
for i in range(k - 1):
    nums.append(nums[i])

l = 0 
cnt = defaultdict(int)

cnt[c] += 1 
for i in range(k):
    cnt[nums[i]] += 1 
ans = len(cnt)

for r in range(k, len(nums)):
    cnt[nums[r]] += 1 
    l = r - (k - 1) 

    cnt[nums[l-1]] -= 1
    if cnt[nums[l-1]] == 0:
        del cnt[nums[l-1]]
    
    ans = max(ans, len(cnt))

print(ans)