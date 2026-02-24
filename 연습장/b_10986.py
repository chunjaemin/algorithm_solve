import sys
input = sys.stdin.readline
from collections import defaultdict
#MOD 연산을 제대로 활용할 줄 알아야만 풀 수 있는 문제
#나머지와 관련된 문제는 수학적으로 MOD 수식을 이용해서 풀 수 있는지 면밀히 검토해봐야 할 듯 
# A = B (MOD M)인 누적합 문제, 같은걸 찾을 땐 딕셔너리에 종류별 개수 적어놓고 combination해서 풀 수 있음

N, M = map(int, input().split())
nums = list(map(int, input().split()))

# print(nums)

same = defaultdict(int)
prefix = [0] * N 
prefix[0] = nums[0]
same[prefix[0] % M] += 1 
for i in range(1, N):
    prefix[i] = prefix[i-1] + nums[i]  
    same[prefix[i] % M] += 1 

# print(same)
ans = 0 
for k, v in same.items():
    ans += v*(v-1) //2
    if k % M == 0:
        ans += v 
print(ans)

# print(prefix)