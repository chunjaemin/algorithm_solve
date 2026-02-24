import sys
input =sys.stdin.readline 

A = list(input().rstrip())
B = list(input().rstrip())
C = list(input().rstrip())

NA = len(A)
NB = len(B)
NC = len(C)

dp = [[[0]* (NC+1) for _ in range(NB+1)] for _ in range(NA+1)]

for i in range(1,NA+1):
    for j in range(1, NB+1):
        for k in range(1, NC+1):
            if A[i-1] == B[j-1] and B[j-1] == C[k-1]:
                dp[i][j][k] = dp[i-1][j-1][k-1] + 1 
            else:
                dp[i][j][k] = max(dp[i-1][j][k], dp[i][j-1][k], dp[i][j][k-1])

print(dp[NA][NB][NC])