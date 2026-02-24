import sys
from collections import defaultdict 
input = sys.stdin.readline 

N = int(input())

S = list(input().rstrip())
# print(S)

l = 0 
sdict = defaultdict(int)
ans = 0
for r in range(len(S)):
    sdict[S[r]] += 1 
    while len(sdict) > N:
        sdict[S[l]] -= 1
        if sdict[S[l]] == 0:
            del sdict[S[l]]
        l += 1 
    ans = max(ans, r - l + 1)

print(ans)