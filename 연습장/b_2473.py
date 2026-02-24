import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

min_val = sys.maxsize
ans1 = 1
ans2 = 1
ans3 = 1

for i in range(N-2):
   
    l, r = 0, N - 1
    while (l<r):
        sum = n_arr[l] + n_arr[r] + n_arr[i]
        if abs(sum) < abs(min_val):
            min_val = sum
            ans1 = n_arr[l]
            ans2 = n_arr[r]
            ans3 = n_arr[i]
        if sum > 0:
            r -= 1
        elif sum < 0:
            l += 1 
        else:
            break

ans_arr = [ans1,ans2,ans3]
ans_arr.sort()

print(ans_arr[0],ans_arr[1],ans_arr[2])    
