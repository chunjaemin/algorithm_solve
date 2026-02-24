import sys
input = sys.stdin.readline

N, K = map(int, input().split())

mod = 0
ans = 1
while True:
    if N > K:
        print("-1")
        exit()
    if K == N:
        print(ans)
        break
    mod = K % 10 
    if mod == 1:
        K = K // 10
        ans += 1
    elif K % 2 == 0:
        K = K // 2
        ans += 1
    else:
        print("-1")
        exit()