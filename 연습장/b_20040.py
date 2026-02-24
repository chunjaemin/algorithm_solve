import sys
input = sys.stdin.readline 

N,M = map(int, input().split())
parent = [x for x in range(N)]

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a,b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b 

turn = 0
ans = sys.maxsize 
for i in range(M):
    turn += 1
    a, b = map(int, input().split())
    
    if find(a) != find(b):
        union(a, b) 
    else:
        ans = min(ans, turn) 

if ans == sys.maxsize:
    print(0)
else:
    print(ans)