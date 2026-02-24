import sys
input = sys.stdin.readline 

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
minus = 0 
plus = 0
zero = 0
def dfs(n, r, c):
    global minus 
    global zero 
    global plus
    tile = board[r][c]

    for i in range(r, r + n):
        for j in range(c, c + n):
            if board[i][j] != board[r][c]:
                for k in range(9):
                    nn = n// 3
                    nr = r + (k // 3) * nn
                    nc = c + (k % 3) * nn 
                    # print(f"nn: {nn}",nr,nc)
                    # for row in board[r:r+n]:
                    #     print(" ".join(map(str, row[c:c+n])))       
                    dfs(nn, nr, nc)
                return 
    
    if tile == -1:
        minus += 1
    if tile == 0:
        zero += 1
    if tile == 1:
        plus += 1

dfs(N,0,0)

print(minus)
print(zero)
print(plus)
