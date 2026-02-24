import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline 

N, M = map(int, input().split())

parent = [x for x in range(N+1)]
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
 

for i in range(M):
    c, a, b = map(int, input().split())
    if c == 0: 
        union(a, b)
    elif c==1:
        print("YES" if find(a) == find(b) else "NO")