import sys
input = sys.stdin.readline
from collections import deque

# 입력 받기
# 4개의 톱니바퀴 상태를 deque로 저장 (회전 효율성을 위해)
gears = [deque(map(int, list(input().strip()))) for _ in range(4)]
k = int(input())

def rotate_right(gear):
    gear.rotate(1) # 시계 방향: [1, 2, 3] -> [3, 1, 2]

def rotate_left(gear):
    gear.rotate(-1) # 반시계 방향: [1, 2, 3] -> [2, 3, 1]

for _ in range(k):
    # num: 톱니 번호(1~4), d: 방향(1:시계, -1:반시계)
    num, d = map(int, input().split())
    idx = num - 1 # 인덱스는 0부터 시작하므로 -1
    
    # 1. 각 톱니바퀴가 회전할 방향을 저장할 리스트 (0이면 회전 X)
    dirs = [0] * 4
    dirs[idx] = d
    
    # 2. 왼쪽 방향으로 전파 (기준 톱니의 왼쪽들을 검사)
    # 현재 보고 있는 톱니(i)와 그 왼쪽 톱니(i-1) 비교
    for i in range(idx, 0, -1):
        # gears[i]의 9시(6)와 gears[i-1]의 3시(2)가 다르면
        if gears[i][6] != gears[i-1][2]:
            dirs[i-1] = -dirs[i] # 반대 방향으로 설정
        else:
            break # 극이 같으면 더 이상 전파되지 않음
            
    # 3. 오른쪽 방향으로 전파
    # 현재 보고 있는 톱니(i)와 그 오른쪽 톱니(i+1) 비교
    for i in range(idx, 3):
        # gears[i]의 3시(2)와 gears[i+1]의 9시(6)가 다르면
        if gears[i][2] != gears[i+1][6]:
            dirs[i+1] = -dirs[i] # 반대 방향으로 설정
        else:
            break
            
    # 4. 실제 회전 수행
    for i in range(4):
        if dirs[i] == 1:
            rotate_right(gears[i])
        elif dirs[i] == -1:
            rotate_left(gears[i])

# 점수 계산
score = 0
if gears[0][0] == 1: score += 1
if gears[1][0] == 1: score += 2
if gears[2][0] == 1: score += 4
if gears[3][0] == 1: score += 8

print(score)