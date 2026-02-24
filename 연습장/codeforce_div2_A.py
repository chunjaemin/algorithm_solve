import sys
from collections import deque 
input = sys.stdin.readline 

T  = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    R = []
    B = []    
    for i, x in enumerate(nums):
        if i % 2 == 0:
            R.append(x)
        else:
            B.append(x)
    R.sort()
    B.sort()
    RQ = deque(R)
    BQ = deque(B)
    # print(R)
    # print(B)
    new_nums = []
    is_ans = "YES"
    if R[0] < B[0]:
        if len(R) < len(B):
            is_ans = "NO"

        while len(RQ) > 0 or len(BQ) > 0:
            if len(RQ) > 0:
                new_nums.append(RQ.popleft())
            if len(BQ) > 0:
                new_nums.append(BQ.popleft())
    else:
        if len(R) > len(B):
            is_ans = "NO"

        while len(RQ) > 0 or len(BQ) > 0:
            if len(BQ) > 0:
                new_nums.append(BQ.popleft())
            if len(RQ) > 0:
                new_nums.append(RQ.popleft())

    # print(new_nums)
    # print(R)
    # print(B)
    for i in range(1, len(new_nums)):
        if new_nums[i-1] > new_nums[i]:
            is_ans = "NO"
    
    print(is_ans)

    

