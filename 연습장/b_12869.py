import sys 
from itertools import permutations
from collections import deque 
input = sys.stdin.readline 

#그리디 문제같음, 체력순으로 나열 후 계속 피 깍아주면 되는 듯 해 보임 

#머야 그리디가 아님, bfs??, dfs로는 풀 수 있을 것 같긴한데 시간초과 안나나? 날 법 한데 
#그래도 일단 구현은 할 수 있는지 궁금하니까 ㄱㄱ 
#역시나 시간초과 
#가지치기로 다시 도전? or bfs로 선회? 일단 어려운건 아니니까 가지치기로 한번 ㄱ 
#가지치기도 시간초과
#순열과 for문도 낭비긴한데 이걸 조합 + sort로 바꾼다고 더 나아지긴하나? 

# def dfs (depth, scvs):
#     global ans 
#     if scvs == []:
#         ans = min(ans, depth)
#         return
#     if depth >= ans:
#         return 
#     perm = permutations(scvs, len(scvs))
#     for case_scvs in perm: 
#         dmg = 9 
#         next_scvs = []
#         for x in case_scvs:
#             x = x - dmg 
#             if x > 0:
#                 next_scvs.append(x)
#             dmg = dmg//3 
#         dfs(depth+1, next_scvs)
        

# dfs(0, scvs)

N = int(input())
nums = list(map(int, input().split()))
nums += [0] * (3 - len(nums))


ans = sys.maxsize
q =deque()
q.append(nums) 
visited = [[[0]* 61 for _ in range(61)] for _ in range(61)]
while q:
    scvs = q.popleft()
    perm = permutations(scvs, len(scvs))
    a, b, c = scvs 
    for case_scvs in perm:
        na, nb, nc = case_scvs
        na, nb, nc = max(0, na - 9), max(0, nb - 3), max(0, nc - 1)
        if na == 0 and nb == 0 and nc == 0:
            print(visited[a][b][c] + 1)
            exit()
        if visited[na][nb][nc] == 0:
            visited[na][nb][nc] += visited[a][b][c] + 1 
            q.append([na,nb,nc])            
print(ans)

