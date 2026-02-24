import sys
input = sys.stdin.readline 

#====================디버깅==========================
DEBUG = 1
def debug(*args):
    if not DEBUG:
        return
    print(*args)
    
def debug_b(name, board):
    if not DEBUG:
        return
    print(f"==={name}===")
    for row in board:
        print(" ".join(map(str, row)))

def debug_i():
    if not DEBUG:
        return
    input()
#==============================================

#====================아이디어==========================
#방향 1 ~ 8 북쪽부터 반시계방향 
#물고기 이동 후 상어 이동 => 반복
#상어가 먹을 수 있는 물고기 번호합 최대 
#물고기 이동 => 가능 
#상어 이동 가능 
#최대는 어케구함? bfs로 가능? 백트래킹해야할 것 같긴한데 
#==============================================

#======================유틸함수============================
def all_fish_move(board):
    pass
    
def shark_move():
    pass
def backtraking():
    pass
#=================================================

#====================문제풀이=========================
R = [-1,-1,0,1,1,1,0,-1]
C = [0,-1,-1,-1,0,1,1,1]

board = [[0]*4 for _ in range(4)]
for i in range(4):
    arr = list(map(int, input().split()))
    for j in range(0,8,2):
        board[i][j//2] = (arr[j],arr[j+1])
debug_b("board", board)


#==============================================