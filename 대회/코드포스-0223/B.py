import sys
from collections import Counter
input =sys.stdin.readline 

#같은문자 3번나오면 못만듬, + ab 제외한 문자는 카운트 초기화 

T = int(input())

for _ in range(T):
    N = int(input())
    S = list(input().rstrip())
    if len(S) % 2 == 0:
        even = 1
    else:
        even = 0 
    
    A = []
    k_cnt = 0
    for x in S:
        if x != "?":
            A.append(x)
        else:
            k_cnt += 1 
            
    S = A
    if even == 1:
        a, b = 1, 1 
    else:
        if S[0] == "a":
            a, b = 2, 0 
        else:
            a, b = 0, 2

        
    ans = "YES"
    for i in range(len(S)):
        # print(S[i], a, b)
        if S[i] == "a":
            if a > 0:
                a -= 1 
                b += 1 
            else:
                ans = "NO"
                break 
        if S[i] == "b":
            if b > 0:
                b -= 1
                a += 1 
            else:
                ans = "NO"
                break 

    print(ans)