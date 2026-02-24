import sys 
input = sys.stdin.readline 

T = int(input())
N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

a_arr = []
b_arr = []

a_sum = [[0] * (N) for _ in range(N)]
for i in range(N):
    a_sum[i][i] = A[i]
    a_arr.append(a_sum[i][i])

b_sum = [[0] * (M) for _ in range(M)]
for i in range(M):
    b_sum[i][i] = B[i]
    b_arr.append(b_sum[i][i])

for i in range(N):
    for j in range(i+1,N):
        a_sum[i][j] = a_sum[i][j-1] + A[j]
        a_arr.append(a_sum[i][j])
    
for i in range(M):
    for j in range(i+1,M):
        b_sum[i][j] = b_sum[i][j-1] + B[j]
        b_arr.append(b_sum[i][j])

# for row in a_sum:
#     print(" ".join(map(str, row)))
# print("")

# for row in b_sum:
#     print(" ".join(map(str, row)))
# print("")

a_arr.sort()
b_arr.sort()

# print("a_arr", a_arr)
# print("b_arr", b_arr)

ans = 0 
l, r = 0, len(b_arr) - 1
while l <= len(a_arr) -1 and r >= 0:
    if a_arr[l] + b_arr[r] > T:
        r -= 1 
    elif a_arr[l] + b_arr[r] < T:
        l += 1 
    else:
        l_cnt = 1
        r_cnt = 1 
        while l+1 <= len(a_arr) - 1 and a_arr[l] == a_arr[l+1]:
            l_cnt += 1
            l += 1    
        while r-1 >= 0 and b_arr[r] == b_arr[r-1]:
            r_cnt += 1
            r -= 1         
        ans += l_cnt * r_cnt 
        l += 1 
        r -= 1 
print(ans)