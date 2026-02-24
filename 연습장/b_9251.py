import sys
input = sys.stdin.readline 

A = list(input().rstrip())
B = list(input().rstrip())

NA = len(A)
NB = len(B)
dp = [[0]*(NB+1) for _ in range(NA+1)]
    
for i in range(1, NA+1):
    for j in range(1, NB+1):
        if A[i-1] == B[j-1]:
            dp[i][j] =  dp[i-1][j-1] + 1 
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
result = []
i, j = NA, NB
while i>0 and j>0:
    if A[i-1] == B[j-1]:
        result.append(A[i-1])
        i -= 1 
        j -= 1 
    else:
        if dp[i][j-1] >= dp[i-1][j]:
            j -= 1 
        else:
            i -= 1 

print(len(result))
if result:
    print("".join(result[::-1]))