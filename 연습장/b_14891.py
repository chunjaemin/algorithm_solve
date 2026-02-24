import sys
input = sys.stdin.readline
from collections import deque

def right_rotate(dq):
    dq.rotate(1)

def left_rotate(dq):
    dq.rotate(-1)
    
gears = [deque(map(int, list(input().strip()))) for _ in range(4)]
gears.insert(0, deque([0]*8))

K = int(input())

for _ in range(K):
    dirs = [0,0,0,0,0]
    idx, dir = map(int, input().split())
    dirs[idx] = dir
    
    #오른쪽 전파 
    for i in range(idx, 4, 1):
        if gears[i][2] != gears[i+1][6]:
            #반대방향으로 돌리기
            dirs[i+1] = -dirs[i]
            pass 
        else:
            break
        
    #왼쪽 전파 
    for i in range(idx, 1, -1):
        if gears[i-1][2] != gears[i][6]:
            #반대방향으로 돌리기
            dirs[i-1] = -dirs[i]
            pass  
        else:
            break
    
    for i in range(1, 5, 1):
        if dirs[i] == 1:
            right_rotate(gears[i])
        elif dirs[i] == -1:
            left_rotate(gears[i])

score = 0
for i in range(1, 5, 1):
    if gears[i][0] == 1:
        score += 2 ** (i-1)

print(score)