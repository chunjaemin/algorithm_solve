import sys
input = sys.stdin.readline

N = int(input())

needs = list(map(int, input().split()))

a, b = map(int, input().split())

cnt = 0 
for x in needs:
    x -= a 
    cnt += 1 
    if x > 0:
        v = x // b
        n = x % b
        if n == 0:
            cnt += v
        else:
            cnt += v + 1

print(cnt)