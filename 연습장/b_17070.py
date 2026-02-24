import sys
input = sys.stdin.readline 

#대각선, 가로, 세로 움직임 
#상태정의는 어떻게 할거야? => dp[r][c] = r,c에 올 수 있는 방법의 수? | 대각선, 세로, 가로 상태에 따라 구분 지어줘야하겠는데? 
# dp[r][c][k] = r,c에 k상태(가로, 세로, 대각선)일 때 올 수 있는 방법의 수? 

# 점화식은 어떻게 세울거야?

# 벽에 안 막혔을 때 
# dp[r][c][0] | 가로   => dp[r][c][0] = dp[r-1][c][0] + dp[r-1][c][2] | 가로 + 대각선 
# dp[r][c][1] | 세로   => dp[r][c][1] = dp[r][c-1][1] + dp[r][c-1][2] | 세로 + 대각선 
# dp[r][c][2] | 대각선  => dp[r][c][0] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2] | 가로 + 세로 + 대각선 

# 벽에 막혔을 때
# dp[r][c][0]~dp[r][c][2] = 0 

#board나  0으로 패딩 시켜두면 편하게 dp 가능할 듯 
N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0,0,0] for _ in range(N+1)] for _ in range(N+1)]
# print(dp[0][0][2])

for i in range(2,N+1):
    if board[0][i-1] == 0: 
        dp[1][i][0] = 1 
    else:
        break

for r in range(2, N+1):
    for c in range(1, N+1):
        if board[r-1][c-1] == 0:
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
            dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
            if board[r-1][c-2] == 0 and board[r-2][c-1] == 0:
                dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
            else:
                dp[r][c][2] = 0 
        else:
            dp[r][c][0], dp[r][c][1], dp[r][c][2] = 0, 0, 0

# for row in dp:
#     print(" ".join(map(str, row)))
    
print(dp[N][N][0] + dp[N][N][1] + dp[N][N][2])