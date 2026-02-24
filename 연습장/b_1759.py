import sys
input = sys.stdin.readline 

L, C = map(int, input().split())

chars = list(input().split())

def dfs(depth, idx, path):
    if depth == L:
        checkg = 0
        checkc = 0
        for c in path:
            if c in ('a','e','i','o','u'):
                checkg += 1
            else:
                checkc += 1
        
        if checkg >= 1 and checkc >=2:
            print("".join(path))
        return 
    for i in range(idx, len(chars)):
        next_path = path + [chars[i]]
        dfs(depth+1, i+1, next_path)

chars.sort()
dfs(0,0,[])

