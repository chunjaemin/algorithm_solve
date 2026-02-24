import sys
from collections import deque 
input = sys.stdin.readline

#각 시행에 logn까지 가능 => 
#넣고 빼고 넣고 빼고 => n번임 
#"절대 부족할 일은 없다" => 시뮬레이션 없이도 가능한가? 
# 정답 = A길이 - B길이 - 유통기한으로 사라지는 것 
# 아니네 N 합이 20만이니까 nlogn까지 가능 
# 

T = int(input())
for _ in range(T):
    N, D = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    remain = deque()
    
    day = -1
    for i in range(N):
        day += 1
        
        #오전
        remain.append((A[i], day))
        
        #오후
        need = B[i]
        while need > 0:
            cur_egg, put_day = remain.popleft()
            if put_day + D >= day:
                if cur_egg >= need:
                    remain.appendleft((cur_egg - need, put_day))
                    need = 0 
                else:
                    need -= cur_egg
    ans = 0  
    for x, put_day in remain:
        if put_day + D - 1 >= day:
            ans += x 
    print(ans)