import sys
from collections import deque 
input = sys.stdin.readline 

R = [0,0,1,1]
C = [0,1,0,1]

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

q = deque()
q.append((N,0,0))
answ = 0
ansb = 0 
while q:
    n,r,c = q.popleft()
    
    chw = 1
    chb = 1 
    for i in range(r,r+n):
        for j in range(c,c+n):
            if board[i][j] == 0:
                chb = 0
            if board[i][j] == 1:
                chw = 0
    
    answ += chw  
    ansb += chb 
    
    if not chw and not chb:
        nn = n//2
        for i in range(4):
            nr, nc = r + R[i] * nn, c + C[i] * nn
            q.append((nn, nr, nc))

print(answ)
print(ansb)