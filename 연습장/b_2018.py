import sys
input = sys.stdin.readline 

N = int(input())

l, r = 1, 1
n_sum = 1

cnt = 0
while r<=N:
    # print(l, r, n_sum)
    if n_sum > N:
        n_sum -= l 
        l += 1 
    elif n_sum < N:
        r += 1 
        n_sum += r 
    elif n_sum == N:
        # print("정답:",l, r)
        cnt += 1 
        n_sum -= l 
        l += 1
        r += 1  
        n_sum += r 

print(cnt)