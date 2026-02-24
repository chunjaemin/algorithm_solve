import sys
from collections import deque
input = sys.stdin.readline

C = [1,-1,0,0]
R = [0,0,1,-1]

def bfs():
    while q:
        c, r = q.popleft()
        for i in range(4):
            nc = c + C[i]
            nr = r + R[i]
            if 0 <= nc < N and 0 <= nr < M:
                if check[nc][nr] == 0 and board[nc][nr] == 0:
                    check[nc][nr] = check[c][r] + 1
                    q.append((nc,nr))

M, N = map(int, input().split())

board = []
check = []
max_val = 0
q = deque()
for _ in range(N):
    board.append(list(map(int, input().split())))
    check.append([0]*M)

if all(0 not in row for row in board):
    print(0)
    exit()

for c in range(N): #세로 
    for r in range(M): #가로 
        if board[c][r] == 1:
            q.append((c,r))
bfs()
for c in range(N):
    for r in range(M):
        v = check[c][r]
        if v == 0 and board[c][r] == 0:
            print(-1)
            exit()
        max_val = max(max_val, v)
print(max_val)