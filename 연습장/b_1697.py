import sys
from collections import deque
input = sys.stdin.readline

N, K  = map(int, input().split())

M = 100001
c = [0]*(M)

X = [1,-1,2]

def bfs(s,e):
    q = deque()
    q.append(s)
    c[s] = 1
    while q:
        x = q.popleft()
        for i in range(3):
            if i == 2:
                nx = i*x
            else:
                nx = x + X[i]
                
            if 0 <= nx < M:
                if c[nx] == 0:
                    c[nx] = c[x] + 1
                    if nx == e:
                        return c[nx] - 1
                    q.append(nx) 

if (N == K):
    print(0)
    exit()

print(bfs(N,K))