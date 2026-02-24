import sys
from collections import defaultdict
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))

count = defaultdict(int) 
l = 0 
ans = 0 
for r in range(N):
    count[nums[r]] += 1 
    while len(count) > 2:
        count[nums[l]] -= 1
        if count[nums[l]] == 0:
            del count[nums[l]]
        l += 1 
    ans = max(ans, r - l + 1)

print(ans)