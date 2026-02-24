import sys
input = sys.stdin.readline 

N = int(input())
M = int(input())

g = [[sys.maxsize] * (N+1) for _ in range(N+1)]

for _ in range(M):
    a, b, w = map(int, input().split())
    g[a][b] = min(g[a][b], w)

# for row in g[1:]:
#     print(" ".join(map(str, row[1:]))) 
    
for k in range(1, N+1):
    for i in range(1, N+1):
        for j in range(1, N+1):
            if g[i][j] > g[i][k] + g[k][j]:
                g[i][j] = g[i][k] +g[k][j]    

for i in range(1, N+1):
    for j in range(1, N+1):
        if g[i][j] == sys.maxsize:
            g[i][j] = 0
        if i == j:
            g[i][j] = 0

for row in g[1:]:
    print(" ".join(map(str, row[1:]))) 
    
    