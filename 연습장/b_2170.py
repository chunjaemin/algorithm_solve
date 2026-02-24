import sys
input = sys.stdin.readline

N = int(input())

lines = [list(map(int, input().split())) for _ in range(N)]

lines.sort(key=lambda p: p[0])


ans = 0 
s, e  = lines[0]
for i in range(1, N):
    ns, ne = lines[i]
    
    if e > ns:
        e = max(ne, e) 
    else:
        ans += e - s 
        s = ns
        e = ne 
ans += e - s 
    
print(ans)