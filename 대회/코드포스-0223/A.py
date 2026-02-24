import sys
from collections import deque  
input =sys.stdin.readline 

#종료조건은 x가 목표점보다 커졌을 때겠네 

dx, dy = [2,3,4], [1,0,-1]
T = int(input())

for _ in range(T):
    X, Y = map(int, input().split())
    q = deque()
    
    ans = "NO"
    if Y > 0:
        A = X - 2*Y
        if A >= 0 and A % 3 == 0:
            ans = "YES"
    elif Y < 0:
        A = X + 4*Y
        if A >= 0 and A % 3 == 0:
            ans = "YES"
    else:
        A = X 
        if A >= 0 and A % 3 == 0:
            ans = "YES"
    
    # ans = "NO"
    # while q:
    #     x, y = q.popleft()
        
    #     if x == X and y == Y:
    #         ans = "YES"
        
    #     for i in range(3):
    #         nx, ny = x + dx[i], y + dy[i]
            
    #         if nx > X:
    #             continue 
            
    #         q.append((nx, ny))
            
            
    print(ans)
