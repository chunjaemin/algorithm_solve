import sys
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

ndict = {}
for i in range(N):
    ndict[A[i]] = i

# print(ndict)

nums = []
for i in range(N):
    nums.append(ndict[B[i]])
    
C = [nums[0]]
for num in nums:
    if num > C[-1]:
        C.append(num)
    else:
        idx = bisect_left(C, num)
        C[idx] = num
print(len(C))