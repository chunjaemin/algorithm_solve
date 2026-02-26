import sys
from collections import deque 
input = sys.stdin.readline

# 사이클 판별하는 문제 
# 뭐지 이것도 위상정렬로 풀리는거 같은데, 위상정렬돌리고 진입차수 0이 아닌게 사이클들이잖아
# 각가의 사이클은 뭔지 모르더라도 사이클이 아닌것들은 나오는데? 답은 구할 수 있을 듯 

T = int(input())
for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums = [x-1 for x in nums]
    og = [[] for _ in range(N)]
    inde = [0] * N
    
    for i in range(N):
        og[i].append(nums[i]) 
        inde[nums[i]] += 1
    
    q = deque()
    for i in range(N):
        if inde[i] == 0:
            q.append(i)

    while q:
        x = q.popleft()
        
        for nx in og[x]:
            inde[nx] -= 1
            if inde[nx] == 0:
                q.append(nx)
    
    # print(inde)
    
    ans = 0 
    for i in range(N):
        if inde[i] == 0:
            ans += 1
    print(ans)
        