import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

l, r = 0, N - 1

min_val = sys.maxsize
ans_1 = -1
ans_2 = -1

while(l<r):
    if (abs(n_arr[l] + n_arr[r]) < abs(min_val)):
        min_val = n_arr[l] + n_arr[r]
        ans_1 = n_arr[l]
        ans_2 = n_arr[r]
    if (n_arr[l] + n_arr[r] > 0):
        r -= 1 
    elif (n_arr[l] + n_arr[r] < 0):
        l += 1 
    else:
        break 
    
print(f"{ans_1} {ans_2}")