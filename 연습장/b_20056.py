import sys
input = sys.stdin.readline 
from collections import deque

#==================디버깅존 시작=================================
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
        
def debug_i():
    if not DEBUG:
        return
    input()
#==================디버깅존 끝=================================

#==================아이디어 시작=================================
# K번의 이동 명령 => for k 
# 각 파이어볼은 (위치, 방향, 속도, 질량)을 가져야함 => 이정도면 파이어볼 객체 하나 만드는 것도? 
# 모두 이동 시킨 후 -> 겹친 것은 합치고, 4개로 쪼갬 => 단계별 bfs 적용 해줘야 할듯 
# 쪼갤 때 규칙 ( 질량 // 5, 속력 // 합친 개수, 방향= 모두짝수 or 모두 홀수 => 0,2,4,6 아니면 => 1,3,5,7)
# 질량 0 => 소멸 
# 남아있는 파이어볼 질량의 합 구하기 

#합치는 것 어떻게 함? [][][] => z차원 도입 후 합치기 
#==================아이디어 끝=================================

#==================문제 풀이 시작=================================
R = [-1,-1,0,1,1,1,0,-1]
C = [0,1,1,1,0,-1,-1,-1]
N, M, K = map(int, input().split())

def check_evenodd(arr):
    even = True
    odd = True
    for x in arr:
        if x % 2 == 0:
            odd = False
        else:
            even = False
    return even or odd 

q = deque()
for i in range(M):
    r, c, m, s, d = map(int, input().split())
    q.append((r-1,c-1,m,s,d))

# debug_b("board",board)
# debug(q)

m_board = [[0]*N for _ in range(N)]
for T in range(K):
    ans = 0 
    board = []
    for i in range(N):
        board.append([[] for _ in range(N)])
    debug("=========before==========")
    debug_b("board", board) 
    while q:
        r, c, m, s, d = q.popleft()
        
        nr = (N + r + s*R[d]) % N 
        nc =  (N + c + s*C[d]) % N 
        board[nr][nc].append((nr,nc,m,s,d))
    debug("==========after==========")
    debug_b("board", board)
    
    # FR1 = [-1,0,1,0], FC1 = [0,1,0,-1]
    # FR2 = [-1,1,1,-1], FC2 = [1,1,-1,-1]
    #합치기 
    for r in range(N):
        for c in range(N):
            nums = len(board[r][c])
            if nums == 1:
                r,c,m,s,d = board[r][c][0]
                q.append((r,c,m,s,d))
                ans += m
            if nums >= 2:     
                dirs = []
                t_m = 0 
                t_s = 0
                for (r,c,m,s,d) in board[r][c]:
                    dirs.append(d)
                    t_m += m
                    t_s += s  
                check_type1 = check_evenodd(dirs)
                t_m = t_m // 5
                t_s = t_s // nums
                
                ans += 4*t_m 
                if t_m == 0:
                    continue
                
                if check_type1:
                    for d in [0,2,4,6]:
                        q.append((r, c, t_m, t_s, d)) 
                else:
                    for d in [1,3,5,7]:
                        q.append((r, c, t_m, t_s, d)) 
    if T == K-1:
        print(ans)
#==================문제 풀이 끝=================================