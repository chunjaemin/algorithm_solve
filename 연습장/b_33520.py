import sys
input = sys.stdin.readline

N = int(input())

W = 0 
H = 0
bar = [] 
for i in range(N):
    a, b = map(int ,input().split())
    if a < b:
        bar.append((b,a))
    else:
        bar.append((a,b))

bar.sort()

for a,b in bar:
    W = max(W, a)
    H = max(H, b)

print(W*H)