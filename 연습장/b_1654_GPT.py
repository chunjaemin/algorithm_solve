import sys
input = sys.stdin.readline

def check(mid, lines, N):
    return sum(x // mid for x in lines) >= N

K, N = map(int, input().split())
lines = [int(input()) for _ in range(K)]

l, r = 1, max(lines)
ans = 0

while l <= r:
    mid = (l + r) // 2
    if check(mid, lines, N):
        ans = mid
        l = mid + 1
    else:
        r = mid - 1

print(ans)