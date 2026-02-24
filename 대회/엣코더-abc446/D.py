import sys
from bisect import bisect_left
input = sys.stdin.readline

#1~n까지 배열만들어두고 각 숫자등장 최소인덱스 기록후 그 배열 lis돌리면 끝인 듯 

N = int(input())
nums = list(map(int, input().split()))

n_idx = [sys.maxsize]*(max(nums)+1)

for i in range(N): #RE뜸 고칠 것 
    n_idx[nums[i]] = min(n_idx[nums[i]], i)
    # print(min(n_idx[nums[i]], i), i)

# print(n_idx)

lis = []
for x in n_idx:
    if len(lis) != 0:
        if x > lis[-1]:
            lis.append(x)
        else:
            put_idx = bisect_left(lis, x)
            lis[put_idx] = x
    else:
        lis.append(x)
print(len(lis))