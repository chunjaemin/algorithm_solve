import sys
input = sys.stdin.readline

H, W = map(int, input().split())

boxes = list(map(int, input().split()))

lmax = [0] * W
rmax = [0] * W 

lmax[0] = boxes[0]
for i in range(1, W):
    lmax[i] = max(boxes[i], lmax[i-1])

rmax[W-1] = boxes[W-1]
for i in range(W-2, -1, -1):
    rmax[i] = max(boxes[i], rmax[i+1])

ans = 0 
for i in range(1, W-1):
    ans += max(0,min(lmax[i], rmax[i]) - boxes[i])

print(ans)