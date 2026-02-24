import sys
from collections import defaultdict 
input = sys.stdin.readline 

R, C = [0,0,1,-1], [1,-1,0,0]

def btr(depth, r, c):
    global ans 
    ans = max(ans, depth)
    
    word[board[r][c]] = 1
    for i in range(4):
        nr, nc = r + R[i], c + C[i]
        if 0<= nr < N and 0<= nc < M and word[board[nr][nc]] == 0: 
            btr(depth +1, nr, nc)
    word[board[r][c]] = 0
    
N, M = map(int, input().split())

word = defaultdict(int)

board = [list(input().rstrip()) for _ in range(N)]
# for r in range(N):
    # for c in range(M):
        # word[board[r][c]] = 1        

visited = [[-1]*M for _ in range(N)]
visited[0][0] = 0
ans = 0 
btr(1, 0, 0)
print(ans) 


# print(board)    

