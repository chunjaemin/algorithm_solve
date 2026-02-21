import sys
from collections import Counter 
input =sys.stdin.readline 

# [prev숫자, prev등장횟수, prev숫자, prev등장횟수...] => []
# [3, 1, 1] => [3, 1, 1, 2] => [2, 1, 3, 1, 1, 2] 
# [2, 1, 3, 1, 1, 2] => [3, 1, 2, 2, 1, 3] => [1, 2, 2, 2, 3, 2]
DEBUG = 0

def debug(*args):
    if DEBUG == 1:
        print()
        print(args)

def debug_r(arr):
    if DEBUG == 1:
        print() 
        for row in arr:
            print(" ".join(map(str, row)))

def get_r(arr, t):
    res = []
    for i in range(len(arr[0])):
        res.append(arr[t][i])
    return res 

def get_c(arr, t):
    res = []
    for i in range(len(arr)):
        res.append(arr[i][t])
    return res 

def custom_sort(arr):
    n_cnt = Counter(arr)
    res = []
    temp = []
    for k, v in n_cnt.items():
        temp.append((k, v))
    temp.sort(key = lambda x : (x[1], x[0]))
    for k, v in temp:
        if k == 0:
            continue
        res.append(k)
        res.append(v)
    return res[:100]

R, C, K = map(int, input().split())
R -= 1
C -= 1 
A = [list(map(int, input().split())) for _ in range(3)]

time = 0 
if 0<=R<len(A) and 0<= C < len(A[0]):
    if A[R][C] == K:
        print(time)
        exit()
N, M = 3, 3 

while True: 
    # input()
    # debug(f"======time: {time + 1}=======")
    if time > 100:
        print(-1)
        exit()
        break 

    time += 1
    if N >= M: #행 차례 
        TA = []
        RA = []
        max_len = 0
        debug_r(A)
        for i in range(N):
            row = get_r(A, i)
            sorted_row = custom_sort(row)
            max_len = max(max_len, len(sorted_row))
            TA.append(sorted_row)
        
        for row in TA:
            if len(row) < max_len:
                RA.append(row + [0] * (max_len - len(row)))
            else:
                RA.append(row)    
        debug_r(RA)
        A = RA
        M = len(A[0])
    
    else: #열 차례 
        TA = []
        RA = []
        max_len = 0
        debug_r(A)
        for i in range(M):
            col = get_c(A, i)
            sorted_col = custom_sort(col)
            max_len = max(max_len, len(sorted_col))
            TA.append(sorted_col)
        
        debug_r(TA)
        for row in TA:
            if len(row) < max_len:
                RA.append(row + [0] * (max_len - len(row)))
            else:
                RA.append(row)    
        debug_r(RA)
        RA = list(map(list, zip(*RA)))
        debug_r(RA)
        A = RA
        N = len(A)
    
    if 0<=R<len(A) and 0<= C < len(A[0]):
        if A[R][C] == K:
            break
    # print("M과 N은:" , N, M)
    
print(time)

# print(custom_sort([1,1,2,2]))
# print(get_r(A, 0))
# print(get_c(A, 0))

# print(A)