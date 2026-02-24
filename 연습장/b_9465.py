import sys
input = sys.stdin.readline 

#상태정의 => dp[r][c] =0,0 ~ r,c에서의 최대값
#규칙 => dp[0][c] = max(dp[1][c-1], dp[1][c-2])
#규칙 => dp[1][c] = max(dp[0][c-1], dp[0][c-2])

T = int(input())

for _ in range(T):
    N = int(input())
    board = [ [0] + list(map(int, input().split())) for _ in range(2)] 

    dp = [[0]* (N+1) for _ in range(2)]
    dp[0][1] = board[0][1]
    dp[1][1] = board[1][1]
    
    for c in range(2, N+1):
        dp[0][c] = max(dp[1][c-1], dp[1][c-2]) + board[0][c]
        dp[1][c] = max(dp[0][c-1], dp[0][c-2]) + board[1][c]
    
    print(max(dp[0][N], dp[1][N]))
    
    # print(board)
    # for i in range()