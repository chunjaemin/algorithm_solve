import sys
input = sys.stdin.readline 

# 오, 왼, 위, 아래 
R, C = [sys.maxsize,0,0,-1,1], [sys.maxsize,1,-1,0,0] #혹시 인덱스0 잘못 사용될까봐 인덱스 에러터지게 처리 

def debug_b(board):
    for row in board:
        print(" ".join(map(str, row)))

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
parent = [x for x in range(N)]
pieces = []

for i in range(K):
    r, c, d = map(int, input().split())
    pieces.append([r,c,d])


# debug_b(board)
# print(pieces)

    