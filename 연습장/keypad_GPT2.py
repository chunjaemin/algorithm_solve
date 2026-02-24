import sys 

numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] 
hand = "right"
def solution(numbers, hand):
    keypad = [
        [1,2,3],
        [4,5,6],
        [7,8,9],
        [10,0,12]
    ]

    # 상, 하, 좌, 우 (row, col 기준)
    R = [-1, 1, 0, 0]
    C = [0, 0, -1, 1]

    answer = ""

    def dfs(r, c, target, cnt):
        nonlocal turn, t_pos
        if cnt >= turn:   # 🔥 가지치기
            return

        if keypad[r][c] == target:
            turn = cnt
            t_pos = [r, c]
            return

        visited[r][c] = True

        for i in range(4):
            nr = r + R[i]
            nc = c + C[i]
            if 0 <= nr < 4 and 0 <= nc < 3 and not visited[nr][nc]:
                dfs(nr, nc, target, cnt + 1)

        visited[r][c] = False   # 🔥 백트래킹

    # 시작 위치
    lh = [3, 0]
    rh = [3, 2]

    left_group = {1,4,7}
    right_group = {3,6,9}
    middle_group = {2,5,8,0}

    for x in numbers:
        if x in left_group:
            visited = [[False]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = None
            dfs(lh[0], lh[1], x, 0)
            lh = t_pos
            answer += "L"

        elif x in right_group:
            visited = [[False]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = None
            dfs(rh[0], rh[1], x, 0)
            rh = t_pos
            answer += "R"

        else:
            # 왼손 거리
            visited = [[False]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = None
            dfs(lh[0], lh[1], x, 0)
            left_dist = turn
            left_pos = t_pos

            # 오른손 거리
            visited = [[False]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = None
            dfs(rh[0], rh[1], x, 0)
            right_dist = turn
            right_pos = t_pos

            if left_dist < right_dist:
                lh = left_pos
                answer += "L"
            elif left_dist > right_dist:
                rh = right_pos
                answer += "R"
            else:
                if hand == "left":
                    lh = left_pos
                    answer += "L"
                else:
                    rh = right_pos
                    answer += "R"

    return answer

print(solution(numbers, hand))