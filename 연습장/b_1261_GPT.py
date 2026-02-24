import sys
from collections import deque
input = sys.stdin.readline

C = [0,0,1,-1]
R = [1,-1,0,0]

def zero_one_bfs(M, N, board):
    INF = 10**9
    dist = [[INF]*M for _ in range(N)]
    dist[0][0] = 0

    dq = deque()
    dq.append((0,0))  # (r,c)

    while dq:
        x, y = dq.popleft()

        for i in range(4):
            nx = x + C[i]
            ny = y + R[i]

            if 0 <= nx < N and 0 <= ny < M:
                cost = board[nx][ny]   # 0 또는 1

                # 현재까지 비용 + cost
                if dist[x][y] + cost < dist[nx][ny]:
                    dist[nx][ny] = dist[x][y] + cost
                    if cost == 1:
                        dq.append((nx, ny))
                    else:
                        dq.append((nx, ny))

    return dist[N-1][M-1]


M, N = map(int, input().split())
board = [list(map(int, input().rstrip())) for _ in range(N)]
print(zero_one_bfs(M, N, board))
