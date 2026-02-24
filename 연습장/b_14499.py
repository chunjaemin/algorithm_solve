import sys
input = sys.stdin.readline
from collections import deque 

# 1동 2서 3북 4남 
R = [0,0,-1,1]
C = [1,-1,0,0]

# 0밑 5윗 | 1서 4동 | 북2 남3
# b, w, n, s, e, t          
dice = [0,0,0,0,0,0]


#동쪽 = b->w, t->e, w->t, e->b
def rightDice (dice):
    b, w, n, s, e, t = dice
    dice = [e, b, n, s, t, w]
    # print("right: ", dice)
    return dice 

#서쪽 = b->e, t->w, w->b, e->t
def leftDice (dice):
    b, w, n, s, e, t = dice
    dice = [w, t, n, s, b, e]
    # print("left: ", dice)
    return dice 
#위쪽 = b->s, t->n, s->t, n->b
def upDice (dice):
    b, w, n, s, e, t = dice
    dice = [n, w, t, b, e, s]
    # print("up: ", dice)
    return dice 
#아랫쪽 = b->n, t->s, s->b, n->t
def downDice (dice):
    b, w, n, s, e, t = dice
    dice = [s, w, b, t, e, n]
    # print("down: ", dice)
    return dice  

N, M, r, c, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
# print(board)

actions = deque(map(int, input().split()))
# print(actions)

while actions:
    idx = actions.popleft() - 1
    nr = r + R[idx]
    nc = c + C[idx]
    # print(idx)
    if 0<= nr < N and 0<= nc < M:
        r = nr
        c = nc 
        # print(idx)
        if idx == 0: #동
            dice = rightDice(dice)
            print(dice[-1])
            if board[r][c] == 0:
                board[r][c] = dice[0]  
            else:
                dice[0] = board[r][c]
                board[r][c] = 0 
                
        if idx == 1: #서
            dice = leftDice(dice)
            print(dice[-1])
            if board[r][c] == 0:
                board[r][c] = dice[0]  
            else:
                dice[0] = board[r][c]
                board[r][c] = 0 
        if idx == 2: #북
            dice = upDice(dice)
            print(dice[-1])
            if board[r][c] == 0:
                board[r][c] = dice[0]  
            else:
                dice[0] = board[r][c]
                board[r][c] = 0 
        if idx == 3: #남 
            dice = downDice(dice)
            print(dice[-1])
            if board[r][c] == 0:
                board[r][c] = dice[0]  
            else:
                dice[0] = board[r][c]
                board[r][c] = 0 