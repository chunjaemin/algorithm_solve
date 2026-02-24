import sys
input = sys.stdin.readline 

#약수의 합이 규칙이 있나?
#1~N까지의 각 약수의 합??

N = int(input())

ans = 0
for i in range(1, N+1):
    ans += i * (N // i)
print(ans)