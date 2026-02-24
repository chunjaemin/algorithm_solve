import sys

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] 
hand = "right"
# 키패드
keypad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [10, 0, 12]  # * = 10, # = 12
]

# 상, 하, 좌, 우
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

def dfs_distance(sr, sc, target):
    visited = [[False]*3 for _ in range(4)]
    best = sys.maxsize

    def dfs(r, c, cnt):
        nonlocal best

        # 가지치기
        if cnt >= best:
            return

        # 목표 도달
        if keypad[r][c] == target:
            best = cnt
            return

        visited[r][c] = True

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < 4 and 0 <= nc < 3 and not visited[nr][nc]:
                dfs(nr, nc, cnt + 1)

        # 백트래킹
        visited[r][c] = False

    dfs(sr, sc, 0)
    return best

def solution(numbers, hand):
    # 시작 위치
    left = (3, 0)   # *
    right = (3, 2)  # #

    answer = ""

    for num in numbers:
        # 왼쪽 열
        if num in (1, 4, 7):
            answer += "L"
            for r in range(4):
                for c in range(3):
                    if keypad[r][c] == num:
                        left = (r, c)

        # 오른쪽 열
        elif num in (3, 6, 9):
            answer += "R"
            for r in range(4):
                for c in range(3):
                    if keypad[r][c] == num:
                        right = (r, c)

        # 가운데 열
        else:
            l_dist = dfs_distance(left[0], left[1], num)
            r_dist = dfs_distance(right[0], right[1], num)

            if l_dist < r_dist:
                answer += "L"
                for r in range(4):
                    for c in range(3):
                        if keypad[r][c] == num:
                            left = (r, c)
            elif l_dist > r_dist:
                answer += "R"
                for r in range(4):
                    for c in range(3):
                        if keypad[r][c] == num:
                            right = (r, c)
            else:
                if hand == "left":
                    answer += "L"
                    for r in range(4):
                        for c in range(3):
                            if keypad[r][c] == num:
                                left = (r, c)
                else:
                    answer += "R"
                    for r in range(4):
                        for c in range(3):
                            if keypad[r][c] == num:
                                right = (r, c)

    return answer

print(solution(numbers, hand))