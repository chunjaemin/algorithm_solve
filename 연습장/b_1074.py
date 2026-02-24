import sys 
input = sys.stdin.readline 

R = [0,0,1,1]
C = [0,1,0,1]
N, ar,ac = map(int, input().split())
cnt = 0 

def dfs (n, r, c):
    global cnt 
    if n == 0:
        if r == ar and c == ac:
            print(cnt)
        cnt += 1
        return 
    
    ndiff = 2**(n - 1)
    
    r_idx = 1 if ar >= r + ndiff else 0 
    c_idx = 1 if ac>= c + ndiff else 0 
    
    ci = 2* r_idx + c_idx 
    
    for i in range(4):
        if i == ci: 
            cnt += 4**(n-1) * i 
            nr, nc = r + R[i] * ndiff, c + C[i] * ndiff
            dfs(n-1, nr, nc)
        
dfs(N, 0, 0)