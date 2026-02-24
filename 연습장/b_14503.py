# [c][r]로 써야 하는데 [r][c]로 써서 틀렸음 주의하기 
# while문의 continue를 쓰고 싶었는데 for문 안에서 continue를 써서 for문 continue가 되었음 
# 뒤로가기는 방향을 바꾸면 안되는데 바꿔서 오류가 났었음 
import sys
input = sys.stdin.readline
#북, 동 남, 서
C = [-1,0,1,0] 
R = [0,1,0,-1]

N, M = map(int, input().split())
sc, sr, d = map(int ,input().split())

board = [list(map(int, input().split())) for _ in range(N)]
clean = [[0]*M for _ in range(N)]

# print(board)
# print(score)

c, r = sc, sr 
while True:
    #도착한 칸 청소하기  
    if clean[c][r] == 0:
        clean[c][r] = 1
    
    go_next = 0
    #주변칸 청소 가능 -> 왼쪽부터 시계방향으로 탐색 
    for i in range(4):
        nd = (4 + d - (i+1)) % 4
        nr = r + R[nd] 
        nc = c + C[nd]
        if  0<= nc < N and  0<= nr < M:
            if board[nc][nr] != 1 and clean[nc][nr] == 0:
                c, r, d = nc, nr, nd #한칸 이동 
                go_next = 1
                break 
    
    if (go_next):
        continue
    
    #여기까지 왔으면 주변칸 청소 불가능
    # 뒤로 한칸 갈 수 있으면 뒤로가기
    nd = (d + 2) % 4
    nr = r + R[nd]
    nc = c + C[nd]
    
    #맵끝 or 벽
    if 0<= nr < M and 0<= nc < N:
        if board[nc][nr] != 1:
            c, r = nc, nr #한칸 이동(뒤로가기)
            continue
        else:
            break # 뒤로 한칸 갈 수 없으면 종료  
    else: 
        break

# for i in range(N):
#     print(clean[i])
    


cnt = 0 
for c in range(N):
    for r in range(M):
        cnt += clean[c][r]  

print(cnt)