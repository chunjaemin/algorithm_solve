import sys
from collections import deque 
input = sys.stdin.readline 

# (A*(B+C) + (B*C))

def check_exp(s):
    if s == '+' or s == '-' or s == '*' or s == '/':
        return True 
    else:
        return False 

S = deque(input().rstrip())
S.appendleft('(')
S.append(')')
stack = deque()

pt = 0
while S:
    x = S.pop()    
    stack.append(x)
    if x == '(':
        temp_s = deque()
        temp_c = deque()
        temp_exp = deque()
        while True:
            stack_x = stack.pop()
            temp_s.append(stack_x)
            if stack_x ==')':
                #(B + C) 꼴 일때 
                # print(temp_s)
                while temp_s:
                    sx = temp_s.pop()
                    if sx == '(' or sx == ')':
                        continue 
                    if check_exp(sx):
                        temp_exp.append(sx)
                    else:
                        temp_c.append(sx) 
                while temp_exp:
                    stack.append(temp_exp.pop())
                while temp_c:
                    stack.append(temp_c.popleft())
                break
        # print(stack)
ans = "".join(map(str, stack))
print(ans[::-1])

# print(S)

#bc+*a