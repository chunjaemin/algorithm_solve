import sys
from collections import deque 
input = sys.stdin.readline 

N, M = map(int, input().split()) 

board = [0] * 101
visited = [-1] * 101
for i in range(N):
    a, b = map(int, input().split())
    board[a] = b 

for i in range(M):
    a, b = map(int, input().split())
    board[a] = b 

q = deque()
q.append(1)
while q:
    x = q.popleft()
    
    for i in range(1, 7):
        nx = x + i 
        if 1 <= nx <= 100:
            v = board[nx]
            if v != 0 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                if visited[v] == -1:  
                    q.append(v)
                    visited[v] = visited[x] + 1 
            elif v == 0 and visited[nx] == -1:
                visited[nx] = visited[x] + 1
                q.append(nx)

print(visited[100] + 1)