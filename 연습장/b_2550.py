import sys
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input())

start = list(map(int, input().split()))
end = list(map(int, input().split()))

mapping = {}
nums = [-1] * N
for i in range(N):
    mapping[start[i]] = i 

for i in range(N):
    nums[mapping[end[i]]] = i
    
l_n = []
track = []
for i in range(N):
    idx = bisect_left(l_n, nums[i])
    if len(l_n) == idx:
        l_n.append(nums[i])
    else:
        l_n[idx] = nums[i]
    track.append(idx)

ans = []
target = len(l_n) - 1    
for i in range(len(track)-1, -1, -1):
    if target == track[i]:
        ans.append(end[nums[i]])
        target -= 1
ans.sort()
print(len(l_n))
print(" ".join(map(str, ans)))
