import sys
from bisect import bisect_left
input = sys.stdin.readline 

N = int(input())
pair_arr = []

for i in range(N):
    a, b = map(int, input().split())
    pair_arr.append((a,b))

pair_arr.sort()

# print(pair_arr)
nums = []
for a, b in pair_arr:
    nums.append(b)
    
# print(nums)

C = [nums[0]]
track = [] 
for num in nums:
    if num > C[-1]:
        C.append(num)
        track.append(len(C) - 1)
    else:
        idx = bisect_left(C,num)
        C[idx] = num
        track.append(idx)
target_len = len(C) - 1

result = [a for a,b in pair_arr]
# print(result)
# c_result = []
for i in range(len(track)-1, -1, -1):
    if track[i] == target_len:
        target_len -= 1
        # print("제거 수: ", pair_arr[i][0])
        result.remove(pair_arr[i][0])
        # c_result.append(pair_arr[i][0])
print(N - len(C))
for i in range(len(result)):
    print(result[i])    