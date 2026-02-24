import sys
from collections import deque
input = sys.stdin.readline

# 방향: 북(0), 동(1), 남(2), 서(3)
# (행, 열) 기준 이동
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

N = int(input())
board = [[0] * N for _ in range(N)]

K = int(input())
for _ in range(K):
    r, c = map(int, input().split())
    # 문제에서는 행, 열 순서로 주어짐 (1-based index)
    board[r-1][c-1] = 2  # [중요] == 가 아니라 = 입니다.

L = int(input())
actions = deque()
for _ in range(L):
    t, rotate = input().split()
    actions.append((int(t), rotate))

# 게임 초기 설정
y, x = 0, 0        # 현재 머리 위치 (행, 열)
board[y][x] = 1    # [중요] 시작 위치 뱀 표시
direction = 1      # 처음에는 오른쪽(동쪽)을 보고 있음
time = 0

# 뱀의 몸통 전체 위치를 담는 큐 (꼬리 ~ 머리)
snake = deque([(0, 0)]) 

# 마지막 명령 이후에도 계속 직진하도록 넉넉한 시간 설정
# 하지만 loop 내에서 break 조건이 확실하므로 while True로 돌려도 됩니다.
# 여기서는 작성하신 구조를 살리기 위해 방향 전환 큐를 활용합니다.

idx = 0 # actions 인덱스 처리를 위한 변수

while True:
    time += 1
    
    # 1. 머리 이동 예상 지점 계산
    ny = y + dy[direction]
    nx = x + dx[direction]
    
    # 2. 벽 충돌 체크
    if not (0 <= ny < N and 0 <= nx < N):
        break
    
    # 3. 자기 몸 충돌 체크
    if board[ny][nx] == 1:
        break
    
    # 4. 이동 처리
    # 사과가 있다면
    if board[ny][nx] == 2:
        board[ny][nx] = 1        # 머리 이동
        snake.append((ny, nx))   # 큐에 머리 추가 (꼬리는 그대로 둠 -> 길이 늘어남)
    
    # 빈칸이라면
    elif board[ny][nx] == 0:
        board[ny][nx] = 1        # 머리 이동
        snake.append((ny, nx))   # 큐에 머리 추가
        
        # 꼬리 삭제 (이동 효과)
        ty, tx = snake.popleft() # 가장 오래된 좌표(꼬리) 꺼내기
        board[ty][tx] = 0        # 맵에서 지우기
        
    # 현재 머리 위치 갱신
    y, x = ny, nx
    
    # 5. 방향 전환 체크
    # actions 큐가 비어있지 않고, 현재 시간이 방향 전환 시간과 같다면
    if actions and time == actions[0][0]:
        t, rotate = actions.popleft()
        
        if rotate == 'L': # 왼쪽 90도
            direction = (direction - 1) % 4
        else:             # 오른쪽 90도 ('D')
            direction = (direction + 1) % 4

print(time)