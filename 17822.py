import sys
from collections import deque 
input =sys.stdin.readline 

# 1. 인접한것을 찾는다. 
# 2. 인접한 수들 중 같은 수가 있는지 본다. 
# 3. 있으면 지우기 모드 | 없으면 평균값을 매겨서 +1 -1을 해준다. 
# 원판도 2차원 배열로 충분히 표현 가능하지 않을까? 각 행이 원판 한겹 바깥쪽 원판, 안쪽 원판 = i차이

# 자료구조는 확정)
# 돌리는건 deque로 rotate이용하면 될 것 같음  
# 인접한 것은 배열의 인덱스로 충분히 찾기 가능 

# 탐색 방법)
# 인접한 것을 어떻게 찾을 것인가 격자이동 방식이 곧 인접한 것을 찾는 행위 
# 수가 없다는 것은 어떻게 표현할 것이고 탐색 방법이 어떻게 달라져야 하는가? 
# n^2 으로 전부 탐색해도 될 것 같고 애매하네 *4 까지하면 시간초과인데 이걸 줄일 순 없나
# 마킹은 어떻게 할 것? 즉시 처리? 

# 탐색이 됐다고 치자
# '-'로 바꾼다 => 

DEBUG = 0

def debug_b(s, arr):
    if DEBUG == 1:
        print(f"====={s}=====")
        for row in arr:
            print(" ".join(map(str, row)))

def debug_i():
    if DEBUG == 1:
        input()

R, C = [0,0,1,-1], [1,-1,0,0]
N, M, T = map(int, input().split())

board = [deque(map(int, input().split())) for _ in range(N)]

# x, d, k => d(0시계 r, 1반시계 l)
for _ in range(T):
    x, d, k = map(int, input().split()) #x번 원판, d방향, k번 
    
    tx = x
    debug_b("회전하기 전", board)
    while tx - 1 < N:
        disk = board[tx-1]  
        if d == 0:
            disk.rotate(k)
        else:
            disk.rotate(-k)
        board[tx-1] = disk 
        tx += x 
    
    debug_b("회전한 후", board)
    
    # 탐색 
    is_remain = 0 
    is_same = 0 
    tq = deque()
    for r in range(N):
        for c in range(M):
            if board[r][c] != 'x': # x는 수가 없다는 뜻  #인접할 때 먼저 지우면 문제가 생김, 다 기록해놓고 한번에 업데이트 해야할 듯 
                is_remain = 1  
    
                for i in range(4):
                    nr = r + R[i]
                    nc = (c + C[i] + M) % M
                    # if r == 1 and c == 4:
                    #     print(r, c, board[r][c], "|", nr, nc, board[nr][nc])
                    
                    if 0<= nr < N:
                        if board[r][c] == board[nr][nc]: # 왜 구석에 있는 5는 x표시가 안됐지?? 
                            is_same = 1 
                            tq.append((r,c))
                            tq.append((nr, nc))
                            # board[r][c] = 'x'
                            # board[nr][nc] = 'x'
    debug_b("탐색 후 패치전", board)
    while tq:
        r, c = tq.popleft()
        board[r][c] = 'x'
    
    debug_b("탐색 후", board)
    
    if not is_remain:
        # print("중간에 스탑")
        break

    if not is_same: #이 로직에 문제가 있음 2 0 2 형태에서 발생     
        # print("인접 없음")
        avg_sum, cnt = 0, 0 
        for r in range(N):
            for c in range(M):
                if board[r][c] != 'x':
                    avg_sum += board[r][c]
                    cnt += 1
        avg = avg_sum / cnt 
        # print("avg", avg)
        for r in range(N):
            for c in range(M):
                if board[r][c] != 'x':
                    if board[r][c] < avg:
                        board[r][c] += 1 
                    elif board[r][c] > avg:
                        board[r][c] -= 1 
        debug_b("인접 없음 처리 후", board)

ans = 0 
for r in range(N):
    for c in range(M):
        if board[r][c] != 'x':
            ans += board[r][c]

print(ans)
        