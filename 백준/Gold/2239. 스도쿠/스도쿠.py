import sys
input = sys.stdin.readline 

def pti(r,c):
    return (r // 3) * 3 + c // 3

def dfs(depth):
    if depth == D:
        for row in board:
            print("".join(map(str, row)))
        exit()
        
    r, c = q[depth]
    for i in range(1, 10):
        chx_r = i not in row_d[r]
        chx_c = i not in col_d[c]
        chx_b = i not in box_d[pti(r,c)]
        if chx_r and chx_c and chx_b:
            row_d[r].add(i)
            col_d[c].add(i)
            box_d[pti(r,c)].add(i)
            board[r][c] = i
            
            dfs(depth+1)
            
            row_d[r].discard(i)
            col_d[c].discard(i)
            box_d[pti(r,c)].discard(i)
            board[r][c] = 0 

N = 9
board = [list(map(int, list(input().rstrip()))) for _ in range(N)]

col_d = [set() for _ in range(9)]
row_d = [set() for _ in range(9)]
box_d = [set() for _ in range(9)]

q = []

for r in range(N):
    for c in range(N):
        if board[r][c] == 0:
            q.append((r,c))
        else:
            row_d[r].add(board[r][c])
            col_d[c].add(board[r][c])
            box_d[pti(r,c)].add(board[r][c])
            
D = len(q)

# print()
dfs(0)