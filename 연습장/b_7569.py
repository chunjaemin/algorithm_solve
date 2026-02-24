import sys
from collections import deque 
input = sys.stdin.readline 

H_i = [0,0,0,0,1,-1]
R = [1,-1,0,0,0,0]
C = [0,0,1,-1,0,0]

DEBUG = 1 
def debug_b(name, board):
    if DEBUG:
        print(f"===={name}===")
        for row in board:
            print(" ".join(map(str, row))) 
def debug(*args):
    if DEBUG:
        print(*args)

# 안익은게 있으면 -1 출력 
M, N, H = map(int, input().split())

board = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[-1]*M for _ in range(N)] for _ in range(H)]

# debug_b("board", board)
# debug_b("visited", visited)

q = deque()
for i in range(N):
    for j in range(M):
        for h in range(H):
            if board[h][i][j] == 1:
                q.append((h,i,j))
                visited[h][i][j] = 0 
while q:
    ch, cr, cc = q.popleft()
    for i in range(6):
        nh, nr, nc = ch + H_i[i], cr + R[i], cc + C[i]
        if 0<= nr < N and 0<= nc < M and 0<= nh < H:
            if board[nh][nr][nc] != -1 and visited[nh][nr][nc] == -1:
                visited[nh][nr][nc] = visited[ch][cr][cc] + 1 
                q.append((nh,nr,nc))

fail = 0 
ans = 0
for i in range(N):
    for j in range(M):
        for h in range(H):
            if board[h][i][j] == 0 and visited[h][i][j] == -1:
                fail = 1 
            if board[h][i][j] == 0 and visited[h][i][j] != -1:
                ans = max(ans, visited[h][i][j])

if not fail:
    print(ans)
else:
    print(-1)
# debug_b("visited while안", visited)