import sys
input =sys.stdin.readline 

g1 = list(map(int, input().rstrip()))
g2 = list(map(int, input().rstrip()))

if len(g1) > len(g2):
    g1, g2 = g2, g1 

n1, n2 = len(g1), len(g2)

ans = n1 + n2 

#시작점 인덱스를 정해주는 부분!
for offset in range(-n1 - 100, n2+100):
    check = 1
    for i in range(n1):
        if 0<= offset + i < n2:
            if g1[i] + g2[offset + i] >= 4:
                check = 0
    
    if check == 1:
        current_len = max(n2 - 1, offset + n1 -1 ) - min(0, offset) + 1
        ans = min(ans, current_len) 

print(ans)