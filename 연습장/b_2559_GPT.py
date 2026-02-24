import sys
input = sys.stdin.readline

N, K = map(int,input().split())
arr = list(map(int, input().split()))

window_sum = sum(arr[:K])
max_val = window_sum

for i in range(K, N):
    window_sum += arr[i]      # 새로 들어오는 값
    window_sum -= arr[i-K]    # 빠지는 값
    max_val = max(max_val, window_sum)

print(max_val)