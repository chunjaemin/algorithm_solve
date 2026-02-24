import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

max_val = 0
for i in range(N):
    for j in range(M):
        max_val = max(max_val,board[i][j])

ans = 0 
def dfs(depth,r,c,v):
    global ans 
    R = [0,0,1,-1]
    C = [1,-1,0,0]
    v += board[r][c]
    if v + (4-depth) * max_val < ans:
        return 
    if depth == 4:
        ans = max(ans, v)
        return
    for i in range(4):
        nr = r + R[i]
        nc = c + C[i]
        if 0<=nr < N and 0<= nc < M:
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1 
                dfs(depth+1, nr, nc, v)
                visited[nr][nc] = 0 

def check_T(r,c):
    R = [(0,0,0,1),(0,0,0,-1),(-1,0,1,0),(-1,0,1,0)]
    C = [(-1,0,1,0),(-1,0,1,0),(0,0,0,1),(0,0,0,-1)]
    ans = 0 
    for i in range(len(R)):
        sum = 0
        for j in range(len(R[0])):
            nr = r + R[i][j]
            nc = c + C[i][j]
            if 0<=nr < N and 0<= nc < M:
                sum += board[nr][nc]
            else:
                sum = 0 
                break
        ans = max(sum, ans)
    return ans
ans = 0 
visited = [[0]*M for _ in range(N)] 
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        dfs(1,i,j,0)
        visited[i][j] = 0 
        ans = max(ans, check_T(i,j))

print(ans)