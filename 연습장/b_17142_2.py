import sys
input = sys.stdin.readline 
from collections import deque 

#=================디버그존 시작==============================
DEBUG = 0

def debug(*args):
    if not DEBUG:
        return 
    print(*args)

def debug_b(name, board):
    if not DEBUG:
        return 
    print(f"==={name}===")
    for row in board:
        print(" ".join(map(str, row)))
    print()
    
def debug_i():
    if not DEBUG:
        return 
    input()
#=================디버그존 끝==============================

#-------------문제풀이 아이디어----------------------------- 

#K개 뽑아서 큐에 넣고 시작 
#각바이러스는 퍼지는데, 0이 다채워지면 끝 
#visited를 만들어서 구분 visited + 1 씩 하면서 퍼짐 => 0인 것만 체크 

#------------------------------------------------------------ 

#========== 풀이 코드 ============================================= 
def comb (depth, idx, path):
    if depth == K:
        virus_block = [] 
        for i in path:
            virus_block.append(virus[i])
        selected_virus.append(virus_block)
        return 
            
    for i in range(idx, len(virus)):
        next = path + [i]
        comb(depth+1, i+1, next)

def bfs(): 
    global ans    
    cnt = 0
    debug("=======before=======")
    debug_b("board",board) 
    debug_b("visited",visited) 
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr, nc = r + R[i], c + C[i]
            if 0<= nr <N and 0<= nc < N and board[nr][nc] != 1 and visited[nr][nc] == -1:
                visited[nr][nc] = visited[r][c] + 1 
                q.append((nr,nc))
                if board[nr][nc] == 0:
                    cnt = max(cnt, visited[nr][nc])
    debug("=========after========")
    debug_b("board", board)
    debug_b("visited", visited) 
    debug(f"cnt: {cnt}")
    debug_i()
    
    check = 1
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0 and visited[r][c] == -1:
                check = 0
                break 
    if check:
        ans = min(ans, cnt)

R, C = [0,0,1,-1],[1,-1,0,0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# debug_b("board", board)

virus = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 2: 
            virus.append((r,c))

ans = sys.maxsize
selected_virus = [] 
comb(0,0,[])

debug(selected_virus)
for T in selected_virus:
    q = deque()
    visited = [[-1]*N for _ in range(N)]
    
    for (r,c) in T: #선택한 바이러스 큐에 삽입 
        q.append((r,c)) 
        visited[r][c] = 0     
    bfs() 
    
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
#=================풀이 코드============================================