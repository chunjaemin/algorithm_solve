import sys
input = sys.stdin.readline 

#오, 왼, 위, 아래
R, C = [0,0,-1,1], [1,-1,0,0]

def c_dir(d):
    mappings = [1, 0, 3, 2]
    return mappings[d]

N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
stack = [[[] for _ in range(N)] for _ in range(N)]
pieces = []
# print(stack)

for i in range(K):
    r, c, d = map(int, input().split())
    pieces.append([r-1, c-1, d-1])
    stack[r-1][c-1].append(i)

for turn in range(1, 1001):
    for i in range(K):
        r, c, d = pieces[i]
        
        nr, nc = r + R[d], c + C[d]
        if not (0<= nr < N and 0 <= nc < N) or board[nr][nc] == 2:            
            d = c_dir(d)
            nr, nc = r + R[d], c + C[d]
            pieces[i][2] = d
            
            if not (0<= nr < N and 0 <= nc < N) or board[nr][nc] == 2:
                continue 
        
        pos = stack[r][c].index(i)
        m_pieces = stack[r][c][pos:]
        stack[r][c] = stack[r][c][:pos]
        
        if board[nr][nc] == 1: #빨간색 
            m_pieces = m_pieces[::-1]
        
        for x in m_pieces:
            stack[nr][nc].append(x)
            pieces[x][0], pieces[x][1] = nr, nc
        
        if len(stack[nr][nc]) >= 4:
            print(turn)
            exit()

        
print(-1)