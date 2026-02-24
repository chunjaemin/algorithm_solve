import sys
input = sys.stdin.readline 

A = list(input().rstrip())
B = list(input().rstrip())

NA = len(A)
NB = len(B)

dp = [[0]*(NB+1) for _ in range(NA+1)]

for i in range(1,NA+1):
    for j in range(1,NB+1):
        if A[i-1] == B[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1 
        else: 
            dp[i][j] = 0 

max_v = max(map(max, dp))

print(max_v)