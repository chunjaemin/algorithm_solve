import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
n_arr = list(input().rstrip())
n = len(n_arr)
# print(n)

l, r = 0, 0    
dict = defaultdict(int)
ans = 0 

dict[n_arr[0]] += 1
ans += 1

real_ans = 0
for i in range(1, N):
    r += 1 
    if dict[n_arr[r]] == 0:
        ans += 1
    dict[n_arr[r]] += 1    

max_ans = r - l + 1 

while (r + 1 < n): 
    r += 1 
    dict[n_arr[r]] += 1 
    if (dict[n_arr[r]] == 1): 
        ans += 1
        while ans > N:
            l += 1
            dict[n_arr[l - 1]] -= 1
            if (dict[n_arr[l - 1]] == 0):
                ans -= 1
    max_ans = max(r - l + 1, max_ans)

print(max_ans)
