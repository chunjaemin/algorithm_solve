import sys
from collections import deque
input = sys.stdin.readline

X = [2,2,1,1,-1,-1,-2,-2]
Y = [1,-1,2,-2,2,-2,1,-1]

def bfs(sx,sy,ex,ey,l):
    q = deque()
    check[sx][sy] = 1
    q.append((sx,sy))
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx = x + X[i]
            ny = y + Y[i]
            if (0 <= nx < l and 0 <= ny < l):
                if check[nx][ny] == 0:
                    check[nx][ny] = check[x][y] + 1 
                    if nx == ex and ny == ey:
                        return check[nx][ny] - 1 
                    q.append((nx,ny))
    return 0 

# def dfs(x,y, n):
#     if (x == ex and y == ey):
#         ans = min(n, ans)
#     for i in range(8):
#         nx = x + X[i]
#         ny = y + Y[i]
#         if (0 <= nx < N and 0 <= ny < N):
#             if (check[nx][ny] == 0):
#                 check[nx][ny] = 1
#                 dfs(nx,ny,n+1)



T = int(input())
for _ in range(T):
    global N  
    N = int(input())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    
    board = []
    check = []

    ans = sys.maxsize
    for i in range(N):
        board.append([0]*(N))     
        check.append([0]*(N))
    
    print(bfs(sx, sy, ex, ey ,N))
    