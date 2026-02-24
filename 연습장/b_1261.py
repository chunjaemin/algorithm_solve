import sys
from collections import deque
input = sys.stdin.readline

C = [0,0,1,-1]
R = [1,-1,0,0]
M, N = map(int, input().split())

board = [list(map(int, input().rstrip())) for _ in range(N)]

def bfs(sc,sr,M,N,board): 
    check = [[0]*M for _ in range(N)]
    dist = [[0]*M for _ in range(N)]
    q = deque()
    q.append((sc,sr))
    check[sc][sr] = 1 
    if sc == N-1 and sr == M-1: return dist[sc][sr] 
    while q:
        c, r = q.popleft()
        for i in range(4):
            nc = c + C[i]
            nr = r + R[i]
            if 0<= nc < N and 0<= nr < M:
                if check[nc][nr] == 1: continue
                check[nc][nr] = 1
                
                if board[nc][nr] == 1:
                    dist[nc][nr] = dist[c][r] + 1
                    q.append((nc,nr)) 
                    if nc == N-1 and nr == M-1: return dist[nc][nr] 
                else: 
                    dist[nc][nr] = dist[c][r]
                    q.appendleft((nc,nr)) 
                    if nc == N-1 and nr == M-1: return dist[nc][nr]
                    
                    
print(bfs(0,0,M,N,board))