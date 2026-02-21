import sys
from collections import defaultdict
input = sys.stdin.readline

#슬라이딩 윈도우 문제 
 
while True:
    N = int(input())
    if N == 0:
        break 
    
    S = list(input().rstrip())
    
    # print(S)


    l = 0
    cnt = 0
    ans = 0  
    sd = defaultdict(int)
    for r in range(0, len(S)):
        
        if sd[S[r]] == 0:
            cnt += 1 
        sd[S[r]] += 1    
        
        while cnt > N:
            sd[S[l]] -= 1
            if sd[S[l]] == 0:
                cnt -= 1 
            l += 1
        # print(l, r, r - l + 1, cnt)
        ans = max(ans, r - l + 1)
    print(ans)