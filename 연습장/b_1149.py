import sys
input = sys.stdin.readline 

N = int(input())

r = [0]*(N+1)
g = [0]*(N+1)
b = [0]*(N+1)


r[1], g[1], b[1] = map(int, input().split())
for i in range(2, N+1):
    rv, gv, bv = map(int, input().split())
    r[i] = min(g[i-1]+ rv, b[i-1] + rv)
    g[i] = min(r[i-1]+ gv, b[i-1] + gv)
    b[i] = min(r[i-1]+ bv, g[i-1] + bv)
    
print(min(r[N],g[N],b[N]))