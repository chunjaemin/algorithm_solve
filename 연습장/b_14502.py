import sys
input = sys.stdin.readline
from collections import deque

DEBUG = False

def debug(*args):
    if DEBUG:
        print(*args)

def debug_board(name, board):
    if not DEBUG:
        return
    print(f"==={name}===")
    for row in board:
        print(" ".join(map(str, row)))
    print()

def debug_input():
    if not DEBUG:
        return
    input()


def comb (depth, idx, path):
    if depth == 3:
        # debug(path)
        a, b, c = path[0], path[1], path[2]
        selected_wall.append((walls[a], walls[b], walls[c]))
        return 
        
    for i in range(idx, len(walls)):
        next = path + [i]
        comb(depth +1, i+1, next)


R, C = [0,0,1,-1], [1,-1,0,0]
    
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
# debug_board("board", board)

walls = []
virus = []
for r in range(N):
    for c in range(M):
        if board[r][c] == 0:
            walls.append((r,c))
        if board[r][c] == 2:
            virus.append((r,c)) 

selected_wall = []
paths = []
comb(0,0, paths) 

# debug(walls)
# debug(selected_wall)
ans = 0
q = deque()

for T in selected_wall:
    visited = [[0]*M for _ in range(N)]
    for (r, c) in T:
        visited[r][c] = 1 
    
    for (r, c) in virus:
        visited[r][c] = 1 
        q.append((r,c))
    
    while q: 
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + R[i], c + C[i]
            debug(0<= nr < N and 0 <= nc < M and board[nr][nc] != 1 and visited[nr][nc] == 0)
            if 0<= nr < N and 0 <= nc < M and board[nr][nc] != 1 and visited[nr][nc] == 0:
                debug(nr, nc)
                visited[nr][nc] = 1 
                q.append((nr,nc)) 
    
    #안전구역 영역 확인
    cnt = 0 
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0 and visited[r][c] == 0:
                cnt += 1 
    debug_board("board",board)
    debug_board("visited",visited)
    debug_input()
    ans = max(ans, cnt)

print(ans)