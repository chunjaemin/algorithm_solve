import sys
from collections import deque 
input = sys.stdin.readline 


R, C = [0,0,1,-1],[1,-1,0,0]
N, M = map(int, input().split())

board = [list(map(int, list(input().rstrip()))) for _ in range(N)]

q = deque()
q.append((0,0,0)) # r,c,벽 부순 횟 수

visited = [[[-1,-1] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1

ans = -1 
while q:
    r, c, t = q.popleft()
    
    if r == N-1 and c == M-1:
        ans = visited[r][c][t]
        break
    
    for i in range(4):
        nr, nc = r + R[i], c + C[i]        
        if t == 0: #벽을 안부쉈을 경우 부수는 케이스 추가 
            if 0<= nr < N and 0<= nc < M:
                if visited[nr][nc][1] == -1 and board[nr][nc] == 1: 
                    visited[nr][nc][1] = visited[r][c][0] + 1      
                    q.append((nr,nc,1))  
                    

        
        #안부쉈을 경우 항상 실행되야 하는 놈 
        if 0<= nr < N and 0<= nc < M:
            if visited[nr][nc][t] == -1 and board[nr][nc] != 1: 
                visited[nr][nc][t] = visited[r][c][t] + 1
                q.append((nr, nc, t))

print(ans)

# for row in board:
#     print(row)

    