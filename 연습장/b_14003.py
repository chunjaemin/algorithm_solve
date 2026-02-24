import sys
from bisect import bisect_left
input = sys.stdin.readline 

N =int(input())
nums = list(map(int, input().split()))
C = [nums[0]]
track = []
for num in nums:
    if num > C[-1]:
        C.append(num)
        track.append(len(C)-1)
    else:
        idx = bisect_left(C, num)
        C[idx] = num 
        track.append(idx)
print(len(C))
target_len = len(C) -1

# print(track)

result = []
for i in range(len(track)-1, -1, -1):
    if target_len == track[i]:
        target_len -= 1
        result.append(nums[i])
print(" ".join(map(str, result[::-1])))
