import sys 
input = sys.stdin.readline

def comb (depth, idx, path):
    if depth == M:
        print(" ".join(map(str, path)))
        return 
    for i in range(idx, N+1):
        next = path + [i]
        comb(depth + 1, i + 1, next)

N, M = map(int, input().split())

comb(0,1,[])