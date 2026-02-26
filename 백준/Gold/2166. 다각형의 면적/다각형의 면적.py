import sys
input = sys.stdin.readline 

N = int(input())

X = []
Y = []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

a_sum = 0 
b_sum = 0 
for i in range(N):
    a_sum += X[i] * Y[(i+1) % N]
    b_sum += Y[i] * X[(i+1) % N]

ans = abs(a_sum - b_sum) / 2

print(f"{ans:.1f}")
