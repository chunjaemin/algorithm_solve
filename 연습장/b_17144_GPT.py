import sys
input = sys.stdin.readline

# 방향: 우, 좌, 하, 상
R = [0, 0, 1, -1]
C = [1, -1, 0, 0]

N, M, T = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

# 공기청정기 위치 (행만 저장)
air = []
for i in range(N):
    if board[i][0] == -1:
        air.append(i)

# 위쪽 공기청정기 (반시계)
def air_up():
    r = air[0]

    # 아래 → 위
    for i in range(r-1, 0, -1):
        board[i][0] = board[i-1][0]

    # 왼 → 오
    for i in range(M-1):
        board[0][i] = board[0][i+1]

    # 위 → 아래
    for i in range(r):
        board[i][M-1] = board[i+1][M-1]

    # 오 → 왼
    for i in range(M-1, 1, -1):
        board[r][i] = board[r][i-1]

    board[r][1] = 0

# 아래쪽 공기청정기 (시계)
def air_down():
    r = air[1]

    # 위 → 아래
    for i in range(r+1, N-1):
        board[i][0] = board[i+1][0]

    # 왼 → 오
    for i in range(M-1):
        board[N-1][i] = board[N-1][i+1]

    # 아래 → 위
    for i in range(N-1, r, -1):
        board[i][M-1] = board[i-1][M-1]

    # 오 → 왼
    for i in range(M-1, 1, -1):
        board[r][i] = board[r][i-1]

    board[r][1] = 0

# 시뮬레이션
for _ in range(T):
    tmp = [[0]*M for _ in range(N)]
    tmp[air[0]][0] = -1
    tmp[air[1]][0] = -1

    # 확산
    for r in range(N):
        for c in range(M):
            if board[r][c] > 0:
                spread = board[r][c] // 5
                cnt = 0
                for d in range(4):
                    nr = r + R[d]
                    nc = c + C[d]
                    if 0 <= nr < N and 0 <= nc < M and board[nr][nc] != -1:
                        tmp[nr][nc] += spread
                        cnt += 1
                tmp[r][c] += board[r][c] - spread * cnt

    board = tmp

    # 공기청정기 작동
    air_up()
    air_down()

# 결과 계산
ans = 0
for i in range(N):
    for j in range(M):
        if board[i][j] > 0:
            ans += board[i][j]

print(ans)
