import sys
input = sys.stdin.readline

N = int(input())

#n은 짝수 n개의 숫자를 n/2로 나눌 것임 => 그때의 board합 차이 최소값 
board = [list(map(int, input().split())) for _ in range(N)]


ans = sys.maxsize
def dfs(depth, idx, path):
    global ans 
    if depth == N // 2:
        t1_pow = 0
        t2_pow = 0
        for i in range(len(board)):
            for j in range(i, len(board)):
                if path[i] == path[j] and path[i] == 0: #1팀
                    t1_pow += board[i][j] + board[j][i]         
                if path[i] == path[j] and path[i] == 1: #2팀
                    t2_pow += board[i][j] + board[j][i] 
        ans = min(ans, abs(t1_pow - t2_pow))
    for i in range(idx, N):
        path[i] = 1
        dfs(depth + 1, i+1, path)
        path[i] = 0 
        
path = [0] * N 
dfs(0,0, path)

print(ans)