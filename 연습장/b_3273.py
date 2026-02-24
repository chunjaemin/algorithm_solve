import sys
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
K= int(input())
n_arr.sort() 

l, r = 0, len(n_arr) - 1 #len(n_arr)대신 N쓰면 된다는 걸 잊고 있었음! 
cnt = 0

while (l < r):
    if (n_arr[l] + n_arr[r] > K):
        r -= 1
    elif(n_arr[l] + n_arr[r] < K):
        l += 1 
    else:
        r -= 1
        l += 1 
        cnt += 1 
        
print(cnt)

