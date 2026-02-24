import sys
input = sys.stdin.readline

N, K = map(int, input().split())

houses = [int(input()) for _ in range(N)]
houses.sort()

def check(mid):
    cnt = 1
    last_pick = houses[0]
    for x in houses:
        if (x - last_pick >= mid):
            cnt += 1
            last_pick = x
    return cnt >= K

l,r = 1, houses[-1] - houses[0]
ans = 0

while l <= r: 
    mid = (l+r) // 2
    if check(mid):
        ans = mid        
        l = mid+1
    else:
        r = mid-1

print(ans)

