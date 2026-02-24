import sys 
input = sys.stdin.readline

def perm (depth, path):
    if depth == M:
        print(" ".join(map(str, path)))
        return 
    for i in range(1, N+1):
        if i not in path:
            next = path + [i]
            perm(depth + 1, next)

N, M = map(int, input().split())

perm(0,[])