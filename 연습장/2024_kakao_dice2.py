from itertools import combinations

dice = [[1, 2, 3, 4, 5, 6], [3, 3, 3, 3, 4, 4], [1, 3, 3, 4, 4, 4], [1, 1, 4, 4, 5, 5]]
def solution(dice):
    me = list(combinations(dice, len(dice)//2))
    others = []
    for e in me:
        other = tuple(x for x in dice if x not in e)
        others.append(other)
    
    print(me)
    print("")
    print(others)
    return 
solution(dice)