import sys
from collections import deque 
input = sys.stdin.readline 

#완벽하게 외부라고 할 수 있는 한 공간에서 bfs 확산을 통해 내부/외부 구분? 
#완벽하게 외부라고 할 수 있는 곳이 없음 
#패딩1을 추가해서 임의로 외부라고 할 수 있는 곳을 추가하는건 어떰? 가능할 것 같은데 
#내부를 0, 외부를 2, 치즈를 1? | 보드 외에 필요한가? visited는? 

#단계
#1. bfs 돌려서 내부, 외부 나누기
#2. n*m 칸 각각 치즈인지 판별하고 주변 칸에 2개이상이 0인지 확인하기 
#3  녹아야 할 치즈들은 0으로 바꾸기, 최적화가 가능해 보이긴 하는데 일단 킾(외부 치즈인지 내부치즈인지 판별하는거)
R, C = [0,0,1,-1], [1,-1,0,0]

def check(r,c):
    check_cnt = 0 
    for i in range(4):
        nr, nc = r + R[i], c + C[i]
        if 0<= nr < N and 0<= nc < M: 
            if board[nr][nc] == 2:
                check_cnt += 1 
    if check_cnt >= 2:
        return True 
    else:
        return False 

def inout():
    visited = [[0] * (M+1) for _ in range(N+1)]
    q = deque()
    q.append((0,0))
    
    while q:
        r, c = q.popleft()
        
        for i in range(4):
            nr, nc = r + R[i], c + C[i]
            if 0 <= nr < N and 0 <= nc < M:
                if visited[nr][nc] == 0 and board[nr][nc] != 1:
                    board[nr][nc] = 2 #외부 = 2
                    visited[nr][nc] = 1 
                    q.append((nr,nc))


N, M = map(int, input().split())
board = [list(map(int, input().split())) + [0] for _ in range(N)]
board.append([0]*(M+1))

turn = 0
while True:
    turn += 1
    finish = 1 
    inout()
    for r in range(N):
        for c in range(M):
            if board[r][c] == 1 and check(r,c):
                board[r][c] = 0 
                finish = 0 
   
    # print("board:")
    # for row in board:
    #     print(" ".join(map(str, row)))
    if finish == 1:
        break 

print(turn - 1)

