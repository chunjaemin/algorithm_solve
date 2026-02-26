import sys
input = sys.stdin.readline 

#dp같긴한데 how??
#dp[i] = i길이인 계단수 개수 라고한다면 => 다음길이는 dp[i] * 2가 되긴함 (끝자리가 0과 9일 땐 예외)
#예외를 커버하기 위해 끝자리가 뭐로 끝났는지 저장할 변수 필요할 것 같고 
#여기서 문제, 0~9까지 다 포함되었는지도 알아야함 변수가 하나더 필요하겠네 => ??? 뭘포함하고 포함안하는지 변수로체크가되나?
#0~9포함에 비트마스킹이 필요하네

#dp[i][j][k] i길이, j번으로 끝난 수열, k 상태에 해당하는 수열의 개수 
#점화식은? 
#dp[i][j][k] = dp[i-1][j-1][k | 1 << j] + dp[i-1][j+1][k | 1 << j]

MOD = 1000_000_000
N = int(input())

dp = [[[0] * 1024 for _ in range(10)] for _ in range(N+1)]

#초기세팅
for i in range(1, 10):
    dp[1][i][1 << i] = 1

for i in range(2, N+1):
    for j in range(10):
        for k in range(1024):
            new_k = k | 1 << j
            if j == 0:
                dp[i][j][new_k] = (dp[i][j][new_k] + dp[i-1][j+1][k]) % MOD
            elif j == 9:
                dp[i][j][new_k] = (dp[i][j][new_k] + dp[i-1][j-1][k]) % MOD 
            else:
                dp[i][j][new_k] = (dp[i][j][new_k] + dp[i-1][j-1][k] + dp[i-1][j+1][k]) % MOD

ans = 0
for i in range(10):
    ans = (ans + dp[N][i][1023]) % MOD

print(ans)