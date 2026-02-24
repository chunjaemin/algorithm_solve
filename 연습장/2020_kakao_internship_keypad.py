import sys 
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] 
hand = "right"
# result = "LRLLLRLLRRL"

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = "left"

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"

#초기화
    # check = [[0]*3 for _ in range(4)]
    # turn = sys.maxsize
    # t_pos = [-1,-1]
    

    

def solution(numbers, hand):
    
    keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,12]]
    R = [0, 1, 0,-1]
    C = [-1, 0, 1, 0]
    check = [[0]*3 for _ in range(4)] 
    turn = sys.maxsize
    t_pos = [-1,-1]
    answer = ''
    
    def dfs(c,r,t, cnt):
        nonlocal turn
        nonlocal t_pos
        for i in range(4):
            nc = c + C[i]
            nr = r + R[i]
            if 0<= nr < 3 and 0<= nc < 4 and not check[nc][nr]:
                check[nc][nr] = 1
                if keypad[nc][nr] == t:
                    t_pos = [nc,nr]
                    turn = min(turn, cnt)
                dfs(nc,nr, t, cnt + 1)
                check[nc][nr] = 0

    lh = [3,0] #nc, nr
    rh = [3,2]

    left_group = [1,4,7]
    middle_group = [0,2,5,8]
    right_group = [3,6,9]
    for x in numbers:
        # 숫자가 왼쪽, 중앙, 오른쪽 열인지 확인
        # 왼쪽 열이면 왼손을, 오른쪽 열이면 오른손을 사용 
        # 중앙 열이면 양쪽 거리 비교 후 짧은 쪽 선택 
        if x in left_group:
            check = [[0]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = [-1,-1]
            dfs(lh[0], lh[1], x, 0)
            lh = t_pos
            answer += "L"
    
        if x in right_group:
            check = [[0]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = [-1,-1]
            dfs(rh[0], rh[1], x, 0)
            rh = t_pos
            answer += "R"
        if x in middle_group: 
            check = [[0]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = [-1,-1]
            dfs(lh[0], lh[1], x, 0)
            left_route = turn
            
            check = [[0]*3 for _ in range(4)]
            turn = sys.maxsize
            t_pos = [-1,-1]
            dfs(rh[0], rh[1], x, 0)
            right_route = turn 
            
            print("x: ", x, "left_route: ", lh[0], lh[1], left_route, "right_route: ", rh[0], rh[1], right_route)
            if left_route > right_route:
                answer += "R"
                rh = t_pos
            elif left_route < right_route:
                answer += "L"
                lh = t_pos
            elif left_route == right_route:
                if hand == "right":
                    answer += "R"
                    rh = t_pos
                elif hand == "left":
                    answer += "L"
                    lh = t_pos  
    return answer

print(solution(numbers, hand))