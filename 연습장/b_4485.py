import sys
import heapq
input = sys.stdin.readline

X = [0,0,1,-1]
Y = [1,-1,0,0]

def bfs_dijkstra(sx,sy,N,board):
    sc = board[sx][sy]
    INF = sys.maxsize
    dist = [[INF]*N for _ in range(N)]
    dist[sx][sy] = sc 
    hq = [(sc,sx,sy)]
    
    while hq:
        c,x,y = heapq.heappop(hq)
        
        if dist[x][y] < c:
            continue
        
        for i in range(4):
            nx = x + X[i]
            ny = y + Y[i]
            if 0<= nx < N and 0<= ny < N:
                tc = c + board[nx][ny]
                if tc < dist[nx][ny]:
                    dist[nx][ny] = tc
                    heapq.heappush(hq, (tc,nx,ny))
    return dist[N-1][N-1]
            

cnt = 0 
while True:
    cnt += 1 
    N = int(input())
    if N == 0:
        exit()
    board = [list(map(int, input().split())) for _ in range(N)]
    ans = bfs_dijkstra(0,0,N,board)
    print(f"Problem {cnt}: {ans}")

            