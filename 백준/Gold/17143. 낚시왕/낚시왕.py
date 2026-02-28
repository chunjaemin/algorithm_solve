import sys
from collections import deque 
input = sys.stdin.readline 

#열 이동
#0~N-1열 땅에서 가장 가까운 상어 체크 후 잡기 
#상어 이동, 이때 겹치는 상어 있으면 가장 큰놈만 살아남음 

DEBUG = 0
def debug_b(s, board):
    if DEBUG == 1:
        print()
        print(f"==={s}===")
        for row in board:
            print(" ".join(map(str, row)))

def debug_i():
    if DEBUG == 1:
        input()

def duplicate(board):
    for r in range(N):
        for c in range(M):
            if board[r][c] != []:
                board[r][c].sort(key = lambda x : -x[2])
                board[r][c] = board[r][c][:1]
    return board 

def move(board):
    copy_board = [[[] for _ in range(M)] for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if board[r][c] != []:
                s, d, z = board[r][c][0]
                nr, nc, nd = decision_rc(r,c,s,d)
                copy_board[nr][nc].append((s,nd,z)) 
                    
    return copy_board

def decision_rc(r, c, s, d):
    period_r = 2 * (N - 1)
    period_c = 2 * (M - 1)

    if d < 2:
        if period_r > 0:
            v_pos = (r + R[d] * s) % period_r
            if v_pos >= N:
                nr = period_r - v_pos
                nd = 1 if d == 0 else 0 
            else:
                nr = v_pos
                nd = d
        else:
            nr, nd = 0, d
        return nr, c, nd
    
    else:
        if period_c > 0:
            v_pos = (c + C[d] * s) % period_c
            if v_pos >= M:
                nc = period_c - v_pos
                nd = 3 if d == 2 else 2 
            else:
                nc = v_pos
                nd = d
        else:
            nc, nd = 0, d
        return r, nc, nd

def catch(board, t):
    global score 
    # print(board)
    for i in range(N):
        if board[i][t] != []:
            s, d, z = board[i][t][0]
            board[i][t] = []
            score += z 
            break 
    return board 

R, C = [-1,1,0,0], [0,0,1,-1]
N, M, K = map(int, input().split())
board = [[[] for _ in range(M)] for _ in range(N)]
score = 0 

for _ in range(K):
    r, c, s, d, z = map(int, input().split()) 
    r -= 1
    c -= 1 
    d -= 1
    board[r][c].append((s,d,z))

for i in range(M):
    debug_b(f"{i}번째 board", board)
    
    catched_board = catch(board, i)
    debug_b(f"{i}번째 물고기 잡은 후 board", catched_board)
    # print("score:", score)
    
    moved_board = move(catched_board)
    debug_b(f"{i}번째 움직인 후 board", moved_board)
    
    board = duplicate(moved_board)
    debug_b(f"{i}번째 중복 지운 후 board", board)
    
    debug_i()

print(score)