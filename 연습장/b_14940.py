import sys
from collections import deque 
input = sys.stdin.readline 

R, C = [0,0,1,-1],[1,-1,0,0]
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
visited = [[-1]*M for _ in range(N)]

s, e = -1, -1 
for r in range(N):
    for c in range(M):
        if board[r][c] == 2:
            s, e, = r, c 
        if board[r][c] == 0:
            visited[r][c] = -2

# for row in visited:
#     print(" ".join(map(str, row)))
    
q = deque()
q.append((s, e))
visited[s][e] = 0 

while q:
    r, c = q.popleft()
    
    for i in range(4):
        nr, nc = r + R[i], c + C[i]
        if 0<= nr < N and 0 <= nc < M:
            if visited[nr][nc] == -1 and board[nr][nc] != 0:
                q.append((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

for r in range(N):
    for c in range(M):
        if visited[r][c] == -2:
            visited[r][c] = 0 
            
# print("")
for row in visited:
    print(" ".join(map(str, row)))
# print(visited)