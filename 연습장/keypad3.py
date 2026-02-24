numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] 
hand = "right"

def solution(numbers, hand):
    keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]
    lh = [3,0]
    rh = [3,2]
    answer = ''
    for x in numbers:
        if x in (1,4,7):
            answer += "L"
            for i in range(4):
                for j in range(3):
                    if x == keypad[i][j]:
                        lh = [i,j]
        elif x in (3,6,9):
            answer += "R"
            for i in range(4):
                for j in range(3):
                    if x == keypad[i][j]:
                        rh = [i,j]
        else:
            target = None
            for i in range(4):
                for j in range(3):
                    if x == keypad[i][j]:
                        target = [i,j]
            l_dist = abs(lh[0] - target[0]) + abs(lh[1] - target[1])
            r_dist = abs(rh[0] - target[0]) + abs(rh[1] - target[1])  
            
            if l_dist > r_dist:
                answer += 'R'
                rh = target 
            elif l_dist < r_dist:
                answer += 'L'
                lh = target 
            else:
                if hand == "right":
                    answer += 'R'
                    rh = target 
                if hand == "left":
                    answer += 'L'
                    lh = target 
    return answer

print(solution(numbers, hand))