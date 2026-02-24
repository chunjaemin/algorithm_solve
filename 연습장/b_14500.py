import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 4*(1 + 1 + 1 + 2 + 2) => 28가지 
def check_long(r,c):
    R = [(0,0,0,0),(0,1,2,3)]
    C = [(0,1,2,3),(0,0,0,0)]
    ans = 0 
    for i in range(2):
        sum = 0
        for j in range(4):
            nr = r + R[i][j]
            nc = c + C[i][j]
            if 0<=nr < N and 0<= nc < M:
                sum += board[nr][nc]
            else:
                sum = 0 
                break
        ans = max(sum, ans)
    return ans
        
def check_square(r,c):
    R = [(0,0,1,1)]
    C = [(0,1,0,1)]
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
def check_L(r,c):
    R = [(-1,0,1,1),(-1,0,1,1),(-1,0,1,-1),(-1,0,1,-1),(0,0,0,1),(0,0,0,1),(0,0,0,-1),(0,0,0,-1)]
    C = [(0,0,0,1),(0,0,0,-1),(0,0,0,1),(0,0,0,-1),(-1,0,1,1),(-1,0,1,-1),(-1,0,1,1),(-1,0,1,-1)]
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
def check_Z(r,c):
    R = [(-1,0,0,1),(1,0,0,-1),(-1,0,0,1),(1,0,0,-1),(0,0,-1,-1),(-1,-1,0,0),(1,1,0,0),(0,0,1,1)]
    C = [(0,0,1,1),(-1,-1,0,0),(-1,-1,0,0),(0,0,1,1),(-1,0,0,1),(-1,0,0,1),(-1,0,0,1),(-1,0,0,1)]
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
for i in range(N):
    for j in range(M):
        ans = max(ans, check_long(i,j))
        ans = max(ans, check_T(i,j))
        ans = max(ans, check_Z(i,j))
        ans = max(ans, check_L(i,j))
        ans = max(ans, check_square(i,j))

print(ans)