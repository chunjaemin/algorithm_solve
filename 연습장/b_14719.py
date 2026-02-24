import sys
input = sys.stdin.readline

H, W = map(int, input().split())

boxes = list(map(int, input().split()))

ans = 0 
for i in range(1, W-1):
    max_left = max(boxes[:i])
    max_right = max(boxes[i:])
    ans += max(0,min(max_left, max_right) - boxes[i])

print(ans)