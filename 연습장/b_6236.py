import sys
input = sys.stdin.readline 

#nlogn으로 풀림, 파라메트릭 서치 쓸 수 있을 듯? 

def check(v):
    cnt = 1
    remain = v 
    for x in nums:
        # print(x)
        if remain - x >= 0:
            remain -= x 
        else:
            cnt += 1 
            remain = v - x
    return cnt 

N, M = map(int, input().split())

nums = []
for i in range(N):
    n = int(input())
    nums.append(n)

l, r = max(nums), 10000 * N

ans = sys.maxsize
while l <= r:
    m = (l + r) // 2
    check_v = check(m)
    # print(m, check(m))
    if check_v > M: #check_v를 줄여야함, l를 키워야함 
        l = m + 1 
    elif check_v <= M: #check_v를 키워야함, r을 줄여야 함  
        ans = m
        r = m - 1 

print(ans)