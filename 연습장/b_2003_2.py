import sys
input = sys.stdin.readline 

N, M = map(int ,input().split())
nums = list(map(int, input().split()))

cnt = 0 
s = 0
e = 0
n_sum = nums[0] 

while True:
    if n_sum >= M:
        if n_sum == M:
            cnt += 1
        n_sum -= nums[s]
        s += 1 
    else:
        e += 1
        if e == N:
            break  
        n_sum += nums[e]
        
print(cnt)