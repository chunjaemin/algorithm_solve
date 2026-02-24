import sys
input = sys.stdin.readline 

check_row = [[False]*10 for _ in range(9)]
check_col = [[False]*10 for _ in range(9)]
check_sq = [[False]*10 for _ in range(9)]
    
def dfs(depth):
    # print(depth)
    if depth == len(targets):
        for row in board:
            print(" ".join(map(str, row)))
        exit()
        return 
    
    r, c = targets[depth]
    sq_r = (r // 3) * 3
    sq_c = c // 3 
    #숫자 0~9삽입 
    for i in range(1,10):
        if not check_row[r][i] and not check_col[c][i] and not check_sq[sq_r + sq_c][i]:
            check_row[r][i] = True
            check_col[c][i] = True
            check_sq[sq_r + sq_c][i] = True 
            board[r][c] = i 
            dfs(depth + 1)
            check_row[r][i] = False
            check_col[c][i] = False 
            check_sq[sq_r + sq_c][i] = False 
            board[r][c] = 0 
            
board = [list(map(int, input().split())) for _ in range(9)]
targets = [(r,c) for r in range(9) for c in range(9) if board[r][c] == 0]

for i in range(9):
    for j in range(9):
        check_row[i][board[i][j]] = True
        check_col[j][board[i][j]] = True 
        check_sq[(i//3)*3 + j//3 ][board[i][j]] = True

# print(check_row)
# print(check_col)
# print(check_sq)
dfs(0)
