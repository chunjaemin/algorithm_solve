import sys
from collections import deque 
input =sys.stdin.readline 

#문자열 폭팔 느낌 

T = int(input())

for _ in range(T):
    N = int(input())
    q = deque(map(int, input().split()))
    r = deque()
    
    while len(q) > 1:
        x = q.pop()
        if q[-1] + 1 == x:
            if r:
                q.append(r.popleft())
        else:
            r.appendleft(x)
    r.appendleft(q[0])
    print(len(r))
    