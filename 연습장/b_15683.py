import sys
input = sys.stdin.readline 


DEBUG = 0
def debug_b(name, board):
    if not DEBUG:
        return
    print(f"==={name}===")
    for row in board:
        print(" ".join(map(str, row)))

DIR1 = [(0,1)]
DIR2 = [(0,1),(0,-1)]
DIR3 = [(0,1),(1,0)]
DIR4 = [(0,1),(0,-1),(1,0)]
DIR5 = [(0,1),(0,-1),(1,0),(-1,0)]

def rotate90 (dirs):
    return [(dc,-dr) for dr, dc in dirs]

def dfs(depth):
    global ans
    if depth == len(cctvs):
        cnt = 0 
        for r in range(N):
            for c in range(M):
                if board[r][c] == 0:
                    cnt += 1
        
        if ans > cnt:
            debug_b("board", board)
        ans = min(ans, cnt)
        return 
    cctv = cctvs[depth]
    r, c, t = cctv
    
    match t:
        case 1:
            dirs = DIR1 
            for i in range(4):
                dirs = rotate90(dirs)
                shoot(cctv, dirs)
                dfs(depth + 1)
                undo_shoot(cctv, dirs)
        case 2:
            dirs = DIR2 
            for i in range(4):
                dirs = rotate90(dirs)
                shoot(cctv, dirs)
                dfs(depth + 1)
                undo_shoot(cctv, dirs)
        case 3:
            dirs = DIR3 
            for i in range(4):
                dirs = rotate90(dirs)
                shoot(cctv, dirs)
                dfs(depth + 1)
                undo_shoot(cctv, dirs)
        case 4:
            dirs = DIR4 
            for i in range(4):
                dirs = rotate90(dirs)
                shoot(cctv, dirs)
                dfs(depth + 1)
                undo_shoot(cctv, dirs)
        case 5:
            dirs = DIR5 
            shoot(cctv, dirs)
            dfs(depth + 1)
            undo_shoot(cctv, dirs)
            
def shoot(cctv, dirs):
    r, c, t = cctv
    # debug_b("before_shoot", board)
    for i in range(len(dirs)):
        marking_shoot(cctv, dirs[i])   
    # debug_b("after_shoot", board)
def undo_shoot(cctv, dirs):
    r, c, t = cctv
    for i in range(len(dirs)):
        undo_marking_shoot(cctv, dirs[i])        
    

def marking_shoot(cctv, dir):
    r, c, t = cctv 
    dr, dc = dir
    # time = 0 
    while True:
        # time += 1
        # print(time)
        nr, nc = r + dr, c + dc
        if 0<= nr < N and 0<= nc < M:
            if board[nr][nc] <= 0:
                board[nr][nc] -= 1 
                r,c = nr,nc 
            elif board[nr][nc] == 6:
                break 
            else:
                r,c = nr,nc 
                continue
        else:
            break 
    
def undo_marking_shoot(cctv, dir):
    r, c, t = cctv 
    dr, dc = dir
    while True:
        nr, nc = r + dr, c + dc
        if 0<= nr < N and 0<= nc < M:
            if board[nr][nc] <= -1 :
                board[nr][nc] += 1
                # debug_b("undo_board", board)
                r,c = nr,nc 
            elif board[nr][nc] == 6:
                break 
            else:
                r,c = nr,nc 
                continue
        else:
            break 
    
N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]
cctvs = [(r,c,board[r][c]) for  r in range(N) for c in range(M) if board[r][c] != 0 and board[r][c] != 6] 

ans = sys.maxsize
dfs(0)
print(ans)