import sys
input = sys.stdin.readline 

g1 = list(map(int, list(input().rstrip())))
g2 = list(map(int, list(input().rstrip())))



if len(g1) < len(g2):
    b_g = g2 
    s_g = g1 
else:
    b_g = g1
    s_g = g2 

ans = len(s_g) + len(b_g)
for l in range(len(s_g)):
    check = 1 
    for i in range(l+1):
        if b_g[i] + s_g[(len(s_g) - 1) - l + i] >= 4:
            check = 0 
            # break
        
    if check == 1:
        ans = min(ans, len(s_g) + len(b_g) - l - 1)

for s in range(len(b_g) - len(s_g) + 1):
    check = 1 
    for i in range(len(s_g)):
        if b_g[s + i] + s_g[i] >= 4:
            check = 0 
            # break
        
    if check == 1:
        ans = min(ans, len(b_g))

for l in range(len(s_g)):
    check = 1
    for i in range(l+1):
        if b_g[len(b_g) -1 - l + i] + s_g[i] >=4:
            check = 0 
    
    if check == 1:
        ans = min(ans, len(s_g) + len(b_g) - l - 1)
        
print(ans)