import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*(N+1)

S = int(input())
dp[1] = S

for i in range(2, N+1):
    row = list(map(int ,input().split()))
    temp = [0]*(N+1) 
    
    for j in range(1, i+1):
        if j == 1:
            temp[j] = dp[j] + row[j-1]
        elif j == i:
            temp[j] = dp[j-1] + row[j-1]
        else:
            temp[j] = max(dp[j] + row[j-1], dp[j-1] + row[j-1])  
    for x in range(N+1):
        dp[x] = temp[x]

print(max(dp))