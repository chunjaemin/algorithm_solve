import sys
from collections import deque
input = sys.stdin.readline

R, C = [0,0,1,-1], [1,-1,0,0]
N = int(input())
board = [list(input().rstrip()) for _ in range(N)]
# print(board)

def bfs(color_map):
    visited = [[-1]*N for _ in range(N)]
    cnt = 0 
    for i in range(N):
        for j in range(N):
            if visited[i][j] == -1:
                cnt += 1 
                
                q = deque()
                q.append((i, j))
                visited[i][j] = 0 
                color = color_map[board[i][j]]
                
                while q:
                    r, c = q.popleft()
                    
                    for di in range(4):
                        nr, nc = r + R[di], c + C[di]
                        if 0<= nr < N and 0<= nc < N:
                            if visited[nr][nc] == -1 and color_map[board[nr][nc]] == color: #이부분이 색맹이랑 달라야함
                                q.append((nr, nc))
                                visited[nr][nc] = 0
                    
    return cnt 

print(bfs({'R': 1, 'G': 2, 'B' : 3}), bfs({'R': 1, 'G': 1, 'B' : 2}))