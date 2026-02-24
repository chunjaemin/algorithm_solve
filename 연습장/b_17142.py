import sys

input = sys.stdin.readline
from collections import deque

DEBUG = 0

R = [0, 0, 1, -1]
C = [1, -1, 0, 0]

N, K = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(N)]

birus = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 2:
            birus.append((i, j))

select_q = deque()


def comb(depth, idx, path):
    if depth == K:
        select_q.append(path)
        return

    for i in range(idx, len(birus)):
        next = path + [i]
        comb(depth + 1, i + 1, next)


comb(0, 0, [])

if DEBUG == 1:
    print(select_q)

ans = sys.maxsize

for T in select_q:
    q = deque()
    visited = [[0] * N for _ in range(N)]

    for i in T:
        r, c = birus[i]
        visited[r][c] = 0
        q.append((r, c))

    max_time = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + R[i]
            nc = c + C[i]
            if 0 <= nr < N and 0 <= nc < N:
                if board[nr][nc] != 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = visited[r][c] + 1
                    if board[nr][nc] == 0:
                        max_time = max(max_time, visited[nr][nc])
                    # max_time = max(max_time, visited[nr][nc])
                    q.append((nr, nc))

    cant = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visited[i][j] == 0:
                cant = 1
                break
    if not cant:
        ans = min(ans, max_time)

if ans == sys.maxsize:
    print(-1)
else:
    print(ans)
