numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5] 
hand = "right"

def solution(numbers, hand):
    keypad = [[1,2,3],[4,5,6],[7,8,9],[10,0,11]]
    t_dict = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        10:(3,0), 0:(3,1), 11:(3,2),
    }
    lh = [3,0]
    rh = [3,2]
    answer = ''
    for x in numbers:
        if x in (1,4,7):
            answer += "L"
            lh = t_dict[x]
        elif x in (3,6,9):
            answer += "R"
            rh = t_dict[x]
        else:
            target = None
            target = t_dict[x]
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