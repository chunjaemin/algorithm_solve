from bisect import bisect_left

dice = [[40, 41, 42, 43, 44, 45], [43, 43, 42, 42, 41, 41], [1, 1, 80, 80, 80, 80], [70, 70, 1, 1, 70, 70]]

def comb(depth, idx, path, N, T):
    if depth == N//2:
        T.append(path)
        return 
    for i in range(idx, N):
        next_path = path + [i]
        comb(depth +1, i+1, next_path, N, T)

def comb_dice(depth, path, dice_picks, N):
    if depth == N//2:
        dice_picks.append(path)
        return 
    for i in range(0, 6):
        next_path = path + [i]
        comb_dice(depth +1, next_path, dice_picks, N)

def solution(dice):
    N = len(dice)
    all_arr = [i for i in range(N)]
    T = []
    dice_picks = [] 
    comb(0,0,[],N, T)
    comb_dice(0,[],dice_picks, N)

    max_ans = 0
    for me in T:
        others = [x for x in all_arr if x not in me]

        me_dice_sum = [] 
        other_dice_sum = [] 
        for row in dice_picks:
            temp_dice_sum1 = 0 
            temp_dice_sum2 = 0
            for i, x in enumerate(row):
                temp_dice_sum1 += dice[me[i]][x]
                temp_dice_sum2 += dice[others[i]][x]
            me_dice_sum.append(temp_dice_sum1)
            other_dice_sum.append(temp_dice_sum2)
        cnt = 0 
        other_dice_sum.sort()

        for s in me_dice_sum:
            cnt += bisect_left(other_dice_sum, s)
        # print(cnt)
        if max_ans < cnt:
            max_ans = cnt
            ans = me
     
    return [x + 1 for x in ans]

print(solution(dice))