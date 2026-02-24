import sys
from collections import deque()
input = sys.stdin.readline

def bfs(c,r,n):
    pass

T = int(input())

for _ in range(T):
    M, N = map(int, input().split())
    board = []
    status = []
    q = deque()
    for i in range(N):
        board.append(list(input().rstrip()))
        status.append(list(input().rstrip()))
        
    for c in range(N):
        for r in range(M):
            if board[c][r] == '*':
                q.append((c,r,-1))
    
    for c in range(N):
        for r in range(M):
            if board[c][r] == '@':
                q.append((c,r, 1))

