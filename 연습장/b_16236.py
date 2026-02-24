import sys
from collections import deque
input = sys.stdin.readline

C = [0,0,1,-1]
R = [1,-1,0,0]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

def bfs(sc, sr, w, k, cnt):
    check = [[0]*N for _ in range(N)]
    timer = [[0]*N for _ in range(N)]
    q = deque()
    feed = []
    q.append((sc,sr))
    check[sc][sr] = w
 
    while q:
        c, r = q.popleft()
        for i in range(4):
            nc = c + C[i]
            nr = r + R[i]
  
            if 0<= nc < N and 0<= nr < N:
                if check[nc][nr] == 0: 
                    if check[c][r] > board[nc][nr] and board[nc][nr] > 0:
                        # print(nc, nr, check[c][r] > board[nc][nr], board[nc][nr])
                        check[nc][nr] = check[c][r]
                        timer[nc][nr] = timer[c][r] + 1 
                        q.append((nc,nr))          
                        feed.append((timer[nc][nr],nc,nr))                  
                    elif check[c][r] == board[nc][nr] or board[nc][nr] == 0:
                        check[nc][nr] = check[c][r]
                        timer[nc][nr] = timer[c][r] + 1 
                        q.append((nc,nr))    

    if len(feed) != 0:
        feed.sort(key =lambda p : (p[0],-p[1], p[2]))
        dist, c, r = feed[0]
        cnt += dist
        print(cnt)
        board[c][r] = 0
        if (k+1) // w > 0:  
            return c,r,w+1,0,cnt
        else:
            return c,r,w,k+1,cnt
    else:
        # print(cnt)
        exit()
        
mc, mr, w, k, cnt = -1, -1, 2, 0, 0 

for c in range(N):
    for r in range(N):
        if board[c][r] == 9:
            mc, mr = c, r  
            board[c][r] = -1 

s = bfs(mc, mr, w, k, cnt)
while True:
    c, r, w, k, cnt = bfs(c, r, w, k, cnt)
    # print(c,r,w,k)