import sys
input = sys.stdin.readline

N, K = map(int,input().split())
n_arr = list(map(int, input().split()))

l, r = 0, K - 1
sum_arr = sum(n_arr[0:K])
max_val = -sys.maxsize
max_val = max(sum_arr, max_val) #첫 케이스에서 비교해주는걸 잊었음! 

for i in range(1, N - K + 1):
    sum_arr = sum_arr + n_arr[r+i] - n_arr[l+i - 1]
    max_val = max(sum_arr, max_val)

print(max_val)