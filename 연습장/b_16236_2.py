import sys 
input = sys.stdin.readline
from collections import deque
import heapq 

# 가장 가까운 적부터 먹음 (거리가 같으면 위쪽 -> 왼쪽 순으로 먹음)
# 자기보다 작은 녀석만 먹을 수 있음 (크기가 같으면 지나가기는 가능(크기가 큰놈들을 못지나감))
# 자기 크기 만큼 물고기를 먹으면 크기가 커짐 
# 0: 빈칸, 1~6: 물고기 크기 9: 자기 위치
# 더이상 먹을 수 있는 물고기가 없으면 끝 

R = [0,0,1,-1]
C = [1,-1,0,0]

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
sr, sc = 0, 0
for r in range(N):
    for c in range(N):
        if board[r][c] == 9: 
             sr, sc = r, c 

time = 0 
size = 2
fill = 0

# debug = 1 
while True:
    find = 0
    check = [[0]*N for _ in range(N)]
    check[sr][sc] = 1
    q = deque()
    feed = []

    q.append((sr,sc))
    # print(sr, sc)

    #길 한번 찾는 로직 
    while q and  find != 1: 
        for i in range(len(q)):
            # print(q)
            r, c= q.popleft()
            
            if board[r][c] < size and board[r][c] != 0 and board[r][c] != 9:
                heapq.heappush(feed, (check[r][c], r,c))
                find = 1 
            
            for i in range(4):
                nr = r + R[i]
                nc = c + C[i]
                # print(nr,nc)
                if 0<= nr < N and 0<= nc < N and board[nr][nc] <= size and check[nr][nc] == 0 and board[nr][nc] != 9:
                    check[nr][nc] += check[r][c] + 1
                    # print(nr, nc, check[nr][nc])
                    q.append((nr,nc))

    
    if find == 0:
        break
    
    dist, fr, fc = heapq.heappop(feed) 
    time += dist - 1
    
    board[sr][sc] = 0 
    sr, sc = fr, fc 
    board[sr][sc] = 9 
    
    fill += 1 
    
    if fill == size:
        fill = 0
        size += 1 
    

    
print(time)