# 문제 잘 못 읽고 잘 못 접근함
# 코드 잘 못인줄 알았으나 방법론이 틀렸었음
# r c cr cc nr nc 쓰는데 cr cc 써야하는데 r c를 씀
# r c로 써야하는데 c r로 써서 무한루프에 빠졌었음 
# visited[r][c]로 적어야하는데 visited라고 적어서 조건문 항상 참이 됐었음 

import sys
input =sys.stdin.readline 
from collections import deque

# dr = [0,-1]
# dc = [1,0]
N, L, R = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# print(board)

time = 0 
check = 1

debug = True
while check and debug:
    time += 1
    check = 0   
    visited = [[0]*N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if visited[r][c] == 0:
                dr = [0,0,1,-1]
                dc = [1,-1,0,0]

                q = deque()
                q.append((r,c))
                visited[r][c] = 1
                sum_move = board[r][c]
                alliance = [(r,c)]
                while q:
                    cr, cc = q.popleft()
                    for i in range(4):
                        nr = cr + dr[i]
                        nc = cc + dc[i]
                        if 0<= nr < N and 0<= nc < N:
                            if visited[nr][nc] == 0 and L <= abs(board[cr][cc] - board[nr][nc]) <= R: 
                                q.append((nr,nc))
                                visited[nr][nc] = 1
                                alliance.append((nr,nc))
                                sum_move += board[nr][nc]
                                check = 1
                                
                avg_move = sum_move // len(alliance)

                for cr,cc in alliance:
                    board[cr][cc] = avg_move

print(time-1)