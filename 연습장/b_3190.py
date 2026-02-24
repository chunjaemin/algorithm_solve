# 행, 열 => c, r 인데 r, c로 받아서 문제가 생겼음
# board[c][r] = 1 로 해야하는데 board[c][r] == 1 로 적어서 사과가 기록되지 않고 있었음 
# 방향 회전시킬 때 dir +- 1해주는건 좋은데 인덱스 초과 위험이 있으니 %4해줘야하고 
# -인덱스 안되도록 +4도 미리 해둬야함 
# 마지막 방향 전환 후 앞으로 가야하는데 앞으로 가는 것은 input에 안나와 있기 떄문에 따로 하나 더 넣어주어햐 함
# 충분히 실행시킬 수 있도록 최대한 크게 넣어주어야함 (t - time 으로 for문을 돌리고 있어서 최대크기 엄밀하게  잘 계산 할 것)

import sys
input = sys.stdin.readline 
from collections import deque 


R = [0,1,0,-1]
C = [-1,0,1,0]

N = int(input())
board = [[0]*N for _ in range(N)]

K = int(input())

for _ in range(K):
    c, r = map(int, input().split())
    r -= 1 
    c -= 1 
    board[c][r] = 2 #사과가 있는 칸

L = int(input())
actions = deque()
for _ in range(L):
    t, rotate = input().split()
    t = int(t)
    actions.append([t, rotate])
actions.append([sys.maxsize, 'D'])

r, c = 0, 0 
tr, tc = 0, 0 
dir = 1 
time = 0 

board[0][0] = 1 
next_tail_pos = deque()

end = 0
#게임 시작
while actions and end != 1:
    t, rotate = actions.popleft()
    t = t - time
    for i in range(t):
        time += 1
        nc = c + C[dir]
        nr = r + R[dir]
        if 0<= nc < N and 0<= nr < N:
            next_tail_pos.append([nc,nr])
            
            if board[nc][nr] == 0: 
                board[nc][nr] = 1 
                c ,r = nc, nr
                
                board[tc][tr] = 0
                tc, tr = next_tail_pos.popleft()
                continue
            elif board[nc][nr] == 1:
                end = 1
                break 
            elif board[nc][nr] ==2:
                board[nc][nr] = 1 
                c, r = nc, nr
                continue 
        else:
            end = 1
            break    
    
    if rotate == 'L': #왼쪽 턴 
        dir = (4 + dir - 1) % 4 
    elif rotate == 'D': #오른쪽 턴
        dir = (4 + dir + 1) % 4 

print(time)