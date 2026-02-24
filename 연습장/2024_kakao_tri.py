n = 4 
tops = [1, 1, 0, 1]
# n = 10 
# tops = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
def solution(n, tops):
    N = 2*n+1
    dp = [0] * (N+1)
    dp[1] = 1
    if tops[0] == 1:
        dp[2] = 3
    else:
        dp[2] = 2 
    for i in range(3, N+1):
        if i % 2 == 0:
            if tops[i//2 - 1] == 0:
                dp[i] = (dp[i-1] + dp[i-2]) % 10007
            if tops[i//2 - 1] == 1:
                dp[i] = (dp[i-1] * 2 + dp[i-2]) % 10007
        else:
            dp[i] = dp[i-1] +dp[i-2]    
    return dp[N]

print(solution(n,tops))