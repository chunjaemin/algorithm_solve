import sys
input = sys.stdin.readline

N, K = map(int, input().split())
num = input().strip()  # 숫자 문자열

stack = []
remove = K

for c in num:
    # 스택에 뭔가 있고, 아직 지울 수 있고, top이 나보다 작으면 pop
    while remove > 0 and stack and stack[-1] < c:
        stack.pop()
        remove -= 1
    stack.append(c)

# 아직 덜 지운 경우: 뒤에서 더 잘라내기
if remove > 0:
    stack = stack[:-remove]

print(''.join(stack))