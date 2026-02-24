import sys
input = sys.stdin.readline 

N = int(input())
a, b, c, d = [], [], [], []
for i in range(N):
    x1,x2,x3,x4 = map(int, input().split())
    a.append(x1)
    b.append(x2)
    c.append(x3)
    d.append(x4)    

ab = []
cd = [] 

for i in range(N):
    for j in range(N):
        ab.append(a[i] + b[j])
        cd.append(c[i] + d[j])

# print(ab)
# print(cd)

ab.sort()
cd.sort()

ans = 0 
l, r = 0, len(cd) - 1 
while l < len(ab) and r >= 0:
    if ab[l] + cd[r] > 0:
        r -= 1
    elif ab[l] + cd[r] < 0:
        l += 1
    else:
        l_cnt = 1
        r_cnt = 1 
        while l + 1 < len(ab) and ab[l] == ab[l+1]:
            l_cnt += 1
            l += 1
        while r - 1 >= 0 and cd[r] == cd[r-1]:
            r_cnt += 1
            r -= 1
        ans += l_cnt * r_cnt
        l += 1
        r -= 1 

print(ans)
    