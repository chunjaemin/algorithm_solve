import sys
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))
C = [nums[0]]

for num in nums[1:]:
    if num > C[-1]:
        C.append(num)
    else:
        idx = bisect_left(C, num)
        C[idx] = num 

print(len(C))