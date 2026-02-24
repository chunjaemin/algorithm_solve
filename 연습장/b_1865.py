import sys
input = sys.stdin.readline 

def velman(s):
    dist[s] = 0
    
    for i in range(N):
        for x, nx, w in e:
            if dist[x] != sys.maxsize and dist[x] + w < dist[nx]:
                dist[nx] = dist[x] + w
                if i == N-1:
                    return True 
    
    return False 


T = int(input())

for _ in range(T):
    N, M, W  = map(int, input().split())
    
    e = []
    g = [[] for _ in range(N+1)]
    dist = [sys.maxsize] * (N+1)
    
    for _ in range(M):
        a, b, w = map(int, input().split())
        g[a].append((w, b))
        g[b].append((w, a))
        e.append((a, b, w))
    
    for _ in range(W):
        a, b, w = map(int, input().split())
        g[a].append((-w, b))
        e.append((a, b, -w))

    ans = "NO"
    for i in range(1, N+1):
        is_not_ans = velman(i)
        if is_not_ans:
            ans = "YES"
    print(ans)
    # print(g)
    # print(e)