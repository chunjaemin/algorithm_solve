import sys
input = sys.stdin.readline 

N, K = map(int, input().split())

ans = 0
for n in range(1,N+1):
    sn = list(str(n))
    nn = list(map(int, sn))
    if sum(nn) == K:
        ans += 1

print(ans)