import sys
input = sys.stdin.readline

N, S = map(int, input().split())

nums = list(map(int, input().split()))

l = 0 
min_len = sys.maxsize 
n_sum = 0

for r in range(N):
    n_sum += nums[r]
    while n_sum >= S:
        min_len = min(min_len, r - l + 1)
        n_sum -= nums[l]
        l += 1 

if min_len == sys.maxsize:
    print(0)
else:       
    print(min_len)
    