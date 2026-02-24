import sys
input =sys.stdin.readline 


def velman(s):
    dist[s] = 0 
    
    for i in range(N):
        for x, nx, w in e:
            if dist[x] != sys.maxsize and dist[x] + w < dist[nx]:
                dist[nx] = dist[x] + w 
                if i == N-1: 
                    return True 
    
    return False 

N, M = map(int, input().split())

g = [[] for _ in range(N+1)]
e = []
dist = [sys.maxsize] * (N+1)
for i in range(M):
    a, b, w = map(int, input().split())
    e.append((a, b, w)) 
    g[a].append((w, b))

not_exist_ans = velman(1)

if not_exist_ans:
    print(-1)
else:
    # print(dist)
    for x in dist[2:]:
        if x == sys.maxsize:
            print(-1)
        else:
            print(x)