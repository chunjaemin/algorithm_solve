import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

def dfs(depth, path):
    if depth == M:
        print(" ".join(map(str, path))) 
        return
    for i in range(1, N+1):
        if len(path) == 0: 
            next = path + [i]
            dfs(depth + 1, next)
        else:
            if path[-1] <= i:
                next = path + [i]
                dfs(depth + 1, next)
        
dfs(0,[])