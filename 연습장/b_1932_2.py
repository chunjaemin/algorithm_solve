import sys
input = sys.stdin.readline

N = int(input())

dp = [[0]*(N+1) for _ in range(N+1)]

S = int(input())
dp[1][1] = S

for i in range(2, N+1):
    row = list(map(int ,input().split()))
    
    for j in range(1, i+1):
        if j == 1:
            dp[i][j] = dp[i-1][j] + row[j-1]
        elif j == i:
            dp[i][j] = dp[i-1][j-1] + row[j-1]
        else:
            dp[i][j] = max(dp[i-1][j] + row[j-1], dp[i-1][j-1] + row[j-1])  

print(max(dp[N]))