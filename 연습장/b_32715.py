import sys
input = sys.stdin.readline 

# 십자가 검색로직을 어떻게 짜느냐가 핵심 
# 브루트 포스 십자가 검색은 실패함 => 어디서 시간을 단축시킬 수 있지?
# 결국 모든 배열이 1로 가득차있으면 625만 연산을 피해갈 수가 없음 
# 조금 더 최적화는 가능하긴한데 확실히 안되는 곳은 일단 버리는 쪽으로 

# 와 이게 DP였네, 나중에 응용 가능할 법한 여지가 많은 문제인 듯?? 시뮬레이션 + DP 문제
# 어쩐지 시뮬레이션 치고 쉽더라니 
def check(r, c):
    k = K
    while k > 0:
        for i in range(4):
            nr, nc = r + R[i] * k, c + C[i] * k
            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    return False 
            else:
                return False 
        k -= 1 
    return True 
            
R, C = [1,-1,0,0], [0,0,1,-1]
N, M = map(int, input().split())
K = int(input())

board = [list(map(int ,input().split())) for _ in range(N)]

left = [[-1]*M for _ in range(N)]
right = [[-1]*M for _ in range(N)]
up = [[-1]*M for _ in range(N)]
down = [[-1]*M for _ in range(N)]

for r in range(N):
    for c in range(M):
        pr, pc = r, c+1
        if 0<=pr<N and 0<= pc < M and 0<=c-K <N:
            if left[pr][pc] != -1:
                left[r][c] = left[pr][pc] - board[pr][pc] + board[r][c-K] 
            


ans = 0
for r in range(K, N - K):
    for c in range(K, M - K):
        if board[r][c] == 1:
            if check(r, c):
                ans += 1 

print(ans)