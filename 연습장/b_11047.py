import sys
input = sys.stdin.readline 

N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

ans = 0
coins = coins[::-1]
for x in coins:
    a = K // x
    b = K % x 
    if a > 0:
        ans += a 
        K = b 
print(ans)