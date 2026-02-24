import sys
sys.setrecursionlimit(10**6)

T=int(input())

def dfs(n,K):
    global ans 
    if n == 0:
        dp[K] ==
        return  
    elif n < 0:
        return 
    for i in (1,2,3):
        dfs(n-i,K)
        
for _ in range(T):
    dp = [0] * (N+1)
    N = int(input())
    dfs(N,N)
    print(dp[N])
    