import sys
from itertools import combinations
from collections import defaultdict
input = sys.stdin.readline 

#각 세로선 모두 자기자신으로 마무리 되어야 함 
# 사다리 완성하고, 10번 시뮬레이션 해야함 | 시뮬레이션 한번에 최대 60의 비용이 듬 | 사다리 완성에 드는 비용을 50만 이하정도로는 줄여야겠는데??

# 생각을 좀 바꿔서 중앙에 사다리 하나를 놓는다는건 사다리로 연결된 두 세로선의 도착위치가 바뀐다는걸 의미함
# 사다리를 놓는 행위가 양옆의 위치를 서로 바꾸는 행위라고 생각한다면?? => 높이별로 사다리에 해당하는 둘 위치를 바꿔서 마지막에 각자가 제자리에 오면 성공임
# 이러면 시뮬레이션 비용을 없앨 수 있지 않나? 600의 비용을 => 30으로 줄일 수 있음 

# 이거 사다리를 놓고 계산하지말고 사다리 안놓은 상태에서 기본 사라리의 결과로 
# 최종 도착 위치를 보고 역산으로 정답을 도출할 수 있지 않을까? => 정답이 되는 사다리 배치를 구하고, 그 배치가 실제로 가능한지 검증하는 방식으로 
# 말이안됨 중간에 자리바꾸는 연산 하나만 넣어도 앞으로 바뀔 위치는 나비효과처럼 가늠이 안됨
# 아니지 가늠이 되지, 중간에 사다리를 놓는다는 건 기본 사다리에 의한 결과에서 두 사다리 위치만 바뀌는거임 => 이러면 할만한데?
# 아니네 이게 사다리 놓은 직후 결과를 알 때만 가능한거고 

# 풀이
# 아이씨 그냥 백트래킹이었음 시간복잡도 아슬아슬하게 컷인가봄

def check(e):
    col = [x for x in range(N+1)]
    for i in range(1, H+1):
        if e[i] == []:
            continue
        
        a, b = i, e[i]
        for x in b:
            col[x], col[x+1] = col[x+1], col[x]
    
    check = True  
    for i in range(1, N+1):
        if col[i] != i:
            check = False 
    return check 

N, M, H = map(int, input().split())

cases =[]
for r in range(1, H+1):
    for c in range(1, N):
        cases.append((r, c))

comb1 = combinations(cases, 1)
comb2 = combinations(cases, 2)
comb3 = combinations(cases, 3)

# print(list(comb1))

#넣을 때 x-1과 x+1은 같은 층에 못있음!
e = defaultdict(list)

for i in range(M):
    a, b = map(int, input().split())
    e[a].append(b)


def test(comb, n):
    # print(e)

    for items in comb:
        added = []
        possible = True 
        for a, b in items:
            if b not in e[a] and b-1 not in e[a] and b+1 not in e[a] :
                e[a].append(b)
                added.append((a, b))
            else:
                possible = False 
                
        if possible and check(e):
            print(n)
            exit()
        
        for a, b in added:
            e[a].remove(b)

if check(e):
    print(0)
    exit()
    
test(comb1, 1)
test(comb2, 2)
test(comb3, 3)

print(-1)

#===================================================================

#===================================================================