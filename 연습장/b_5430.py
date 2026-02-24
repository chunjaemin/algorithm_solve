import sys
from collections import deque 
input = sys.stdin.readline 

T = int(input())

for _ in range(T):
    command = input()
    N = int(input())
    sarr = input().rstrip()
    if sarr == "[]":
        arr = deque([])
    else:
        arr = deque(map(int, sarr[1:-1].split(',')))
    # print(arr)
    err =False
    flag = 1
    while command:
        cur_c = command[0]
        command = command[1:]
        if cur_c == 'R':
            flag = -flag
        elif cur_c == 'D':
            if len(arr) > 0:
                if flag == 1:
                    arr.popleft()
                else:
                    arr.pop()
            else:
                err = True
    if not err:
        if flag == 1:
            print("[" + ",".join(map(str, arr)) +"]")
        elif flag == -1:
            arr.reverse()
            print("[" + ",".join(map(str, arr)) +"]")
    else:
        print("error")