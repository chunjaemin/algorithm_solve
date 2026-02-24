import sys
from collections import deque
sys.setrecursionlimit(10000)
input = sys.stdin.readline


T = int(input())

X = [-1,1,0,0]
Y = [0,0,-1,1]

def dfs(x,y,m,n):
    for i in range(4):
        nx = x + X[i]
        ny = y + Y[i]
        if 0 <=nx < m and 0 <= ny < n:
            if c[nx][ny] == 0 and ground[nx][ny] == 1:
                c[nx][ny] = 1 
                dfs(nx, ny, m, n)    

def bfs(s_x,s_y,m,n):
    q = deque()
    q.append((s_x,s_y))
    c[s_x][s_y] == 1
    while q:
        x, y = q.popleft()
        
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            if 0 <=nx < m and 0 <= ny < n:
                if c[nx][ny] == 0 and ground[nx][ny] == 1:
                    c[nx][ny] = 1 
                    q.append((nx,ny))    

def solve():
    M, N, K = map(int, input().split())
    global ground, c 
    ground = []
    c = []
    cnt = 0
    for i in range(M):
        ground.append([0]*N)    
        c.append([0]*N)    

    for i in range(K):
        x, y = map(int, input().split())
        ground[x][y] = 1

    for i in range(M):
        for j in range(N):
            if c[i][j] == 0 and ground[i][j] == 1:
                cnt += 1
                bfs(i,j, M, N)
    print(cnt)

for i in range(T):
    solve()

