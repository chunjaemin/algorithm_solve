import sys
input = sys.stdin.readline
from collections import deque 

#맵 만들고
#공기청정기 배치하고 
#시간별 업데이트 
#구하는 것 = T시간 후 방에 남아있는 미세먼지의 양
#공기청정기는 -1이라고 두는게 좋을 듯 

#한번의 흐름 
#확산 -> 맵 반영 
#공기청정기 작동 -> 맵 반영  
# 확산은 어떻게 할 것인가? bfs 돌리기?

#bfs는 어떻게 돌릴 것인가?
#레벨 별 bfs 돌리기? 
R = [0,0,1,-1]
C = [1,-1,0,0]



N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

filter = []
q = deque()
for r in range(N):
    for c in range(M):
        if board[r][c] != 0 and board[r][c] != -1:
            q.append((r,c,board[r][c]))
        if board[r][c] == -1:
            filter.append(r)
            pass

# def air_up ():
#     dr = [0,-1,0,1]
#     dc = [1,0,-1,0]
#     dir = 0 
    
#     r, c = filter[0], 1
#     board[r][c] = 0  
#     prev = 0 
#     while True:
#         nr = r + dr[dir] 
#         nc = c + dc[dir] 

#         if nr == filter[0] and nc == 0:
#             break
        
#         if 0 <= nr < filter[0] + 1 and 0<= nc < M:
#             prev, board[nr][nc] = board[nr][nc], prev
#             r, c = nr, nc 
#         else: 
#             dir = (4 + dir + 1) % 4 
#             continue
#     # for i in range(N):
#     #     print(board[i])

# def air_down ():
#     dr = [0,1,0,-1]
#     dc = [1,0,-1,0]
#     dir = 0 
    
#     r, c = filter[1], 1
#     board[r][c] = 0  
#     prev = 0 
#     while True:
#         nr = r + dr[dir] 
#         nc = c + dc[dir] 

#         if nr == filter[1] and nc == 0:
#             break
        
#         if filter[1] <= nr < N and 0<= nc < M:
#             prev, board[nr][nc] = board[nr][nc], prev
#             r, c = nr, nc 
#         else: 
#             dir = (4 + dir + 1) % 4 
#             continue
#     # for i in range(N):
#     #     print(board[i])
#     # print("")

# r1,0 ~ 0,0 
 # board[i][0] = board[i-1][0]
# 0,0 ~ 0,M-1 
 # board[0][i] = board[0][i+1]
# 0,M-1 ~ r1,M-1
 # board[i][M-1] = board[i+1][M-1]
# r1,M-1 ~ r1,0 
 # board[r1][i] = board[r1][i-1] 

def air_up2():
    r1 = filter[0]
    for i in range(r1-1, 0, -1):
        board[i][0] = board[i-1][0]
    for i in range(0, M-1, 1):
        board[0][i] = board[0][i+1]
    for i in range(0, r1, 1):
        board[i][M-1] = board[i+1][M-1]
    for i in range(M-1, 1, -1):
        board[r1][i] = board[r1][i-1] 
    board[r1][1] = 0

def air_down2():
    r2 = filter[1]
    for i in range(r2+1, N-1, 1):
        board[i][0] = board[i+1][0]
    for i in range(0, M-1, 1):
        board[N-1][i] = board[N-1][i+1]
    for i in range(N-1, r2, -1):
        board[i][M-1] = board[i-1][M-1]
    for i in range(M-1, 1, -1):
        board[r2][i] = board[r2][i-1]
    board[r2][1] = 0
 # r2,0 ~ N-1,0
  # board[i][0] = board[i+1][0]
 # N-1,0 ~ N-1,M-1
  # board[N-1][i] = board[N-1][i+1]
 # N-1, M-1 ~ r2, M-1
  # board[i][M-1] = board[i-1][M-1]
 # r2, M-1 ~ r2, 0
  # board[r2][i] = board[r2][i-1]

# 위쪽 공기청정기 (반시계)
def air_up():
    r = filter[0]

    # 아래 → 위
    for i in range(r-1, 0, -1):
        board[i][0] = board[i-1][0]

    # 왼 → 오
    for i in range(M-1):
        board[0][i] = board[0][i+1]

    # 위 → 아래
    for i in range(r):
        board[i][M-1] = board[i+1][M-1]

    # 오 → 왼
    for i in range(M-1, 1, -1):
        board[r][i] = board[r][i-1]

    board[r][1] = 0

# 아래쪽 공기청정기 (시계)
def air_down():
    r = filter[1]

    # 위 → 아래
    for i in range(r+1, N-1):
        board[i][0] = board[i+1][0]

    # 왼 → 오
    for i in range(M-1):
        board[N-1][i] = board[N-1][i+1]

    # 아래 → 위
    for i in range(N-1, r, -1):
        board[i][M-1] = board[i-1][M-1]

    # 오 → 왼
    for i in range(M-1, 1, -1):
        board[r][i] = board[r][i-1]

    board[r][1] = 0
    
#실행     
time = 0 
while T != time:
    time += 1
    # tboard = [[0]*M for _ in range(N)]
    # tboard[filter[0]][0] = -1
    # tboard[filter[1]][0] = -1
    tboard = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            tboard[i][j] = board[i][j]
            
    for r in range(N):
        for c in range(M):
            if board[r][c] != 0 and board[r][c] != -1:
                sv = board[r][c]//5 
                
                cnt = 0
                for i in range(4):
                    nr = r + R[i]
                    nc = c + C[i]
                    
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != -1: 
                        tboard[nr][nc] += sv
                        cnt += 1
                        tboard[r][c] = max(0, tboard[r][c] - sv) 
                # tboard[r][c] += board[r][c] - sv * cnt
    for i in range(N):
        for j in range(M):
            board[i][j] = tboard[i][j]
        
    air_up2() 
    air_down2()

# # 시뮬레이션
# for _ in range(T):
#     tmp = [[0]*M for _ in range(N)]
#     tmp[filter[0]][0] = -1
#     tmp[filter[1]][0] = -1

#     # 확산
#     for r in range(N):
#         for c in range(M):
#             if board[r][c] > 0:
#                 spread = board[r][c] // 5
#                 cnt = 0
#                 for d in range(4):
#                     nr = r + R[d]
#                     nc = c + C[d]
#                     if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != -1:
#                         tmp[nr][nc] += spread
#                         cnt += 1
#                 tmp[r][c] += board[r][c] - spread * cnt

#     board = tmp

#     # 공기청정기 작동
#     air_up()
#     air_down()

cnt = 0 
for i in range(N):
    for j in range(M):
        if board[i][j] != -1:
            cnt += board[i][j]

# print(board)    
print(cnt)