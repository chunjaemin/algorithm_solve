import sys
from collections import deque 
input = sys.stdin.readline

#문제보니 각순서규칙을 지키도록 해서 합치는 문제 = 위상정렬인듯

N, M = map(int, input().split())

og = [set() for _ in range(N+1)] #진출그래프
inde = [0] * (N+1)
for _ in range(M):
    nums = list(map(int, input().split()))
    nums = nums[1:]
    for i in range(len(nums) - 1):
        if nums[i] not in og[nums[i+1]]:
            og[nums[i+1]].add(nums[i])
            inde[nums[i]] += 1 
# print(inde)

r_ans = []
q = deque()
for i in range(1, N+1):
    if inde[i] == 0:
        q.append(i) 
        r_ans.append(i)
        
while q:
    x = q.popleft()
    
    for nx in og[x]:
        inde[nx] -= 1
        if inde[nx] == 0:
            q.append(nx)
            r_ans.append(nx)

#사이클판별 (다끝나면 모두 진입차수가 0이어야함)
if sum(inde) != 0:
    print(0)
    exit()

ans = r_ans[::-1]
for x in ans:
    print(x)