import sys 
input = sys.stdin.readline 

N = int(input())

dp = [0] * (N+1)

for i in range(1, N+1):
    dp[i] = 