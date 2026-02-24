import sys
input = sys.stdin.readline

H, W = map(int, input().split())

boxes = list(map(int, input().split()))

stack = []
ans = 0

for i in range(W):
    while stack and boxes[i] > boxes[stack[-1]]:
        bottom = stack.pop()
        if not stack:
            break
        
        left = stack[-1]
        width = i - left - 1
        height = min(boxes[left], boxes[i]) - boxes[bottom]
        ans += width * height
    
    stack.append(i)

print(ans)
