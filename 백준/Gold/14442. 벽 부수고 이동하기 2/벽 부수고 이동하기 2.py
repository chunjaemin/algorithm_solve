import sys
from collections import deque 
input = sys.stdin.readline 

R, C = [0,0,1,-1], [1,-1,0,0]
N, M, K = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(N)]
visited = [[[0]*(K+1) for _ in range(M)] for _ in range(N)]
q = deque()
q.append((0,0,K))
visited[0][0][K] = 1 

ans = -1
while q:
    r, c, chance = q.popleft() 
    
    if r == N-1 and c == M-1:
        ans = visited[r][c][chance]
        break 
    
    for i in range(4):
        nr, nc = r + R[i], c + C[i]
        if 0 <= nr < N and 0 <= nc < M:
            if board[nr][nc] == 0: #벽 안뚫고 가는 경우 
                if visited[nr][nc][chance] == 0: #방문했는지 체크 
                    q.append((nr, nc, chance))
                    visited[nr][nc][chance] += visited[r][c][chance] + 1
            else: #벽 뚫고 가는 경우 
                n_chance = chance - 1 
                if n_chance >= 0:
                    if visited[nr][nc][n_chance] == 0 :
                        q.append((nr, nc, n_chance))
                        visited[nr][nc][n_chance] += visited[r][c][chance] + 1

# for row in visited:
#     print(row)

print(ans)