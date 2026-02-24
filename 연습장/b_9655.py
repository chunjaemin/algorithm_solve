import sys
input = sys.stdin.readline 

N = int(input())

n_arr = [0]*(N+1)
if N >= 1:
    n_arr[1] = 1 
if N>=2:
    n_arr[2] = 0 
if N>=3:
    n_arr[3] = 1


for i in range(4, N+1): 
    #누구턴인지 어떻게 암? 알 필요가 없네 내 턴이라고 생각하고 지는거면 상대방턴이면 무조건 이기겠지 
    #2명 밖에 없어서 스위치 구조인게 누구턴인지 알 필요가 없게 만드는 듯 
    if n_arr[i-3] == 0:
        n_arr[i] = 1
    elif n_arr[i-1] == 0:
        n_arr[i] = 1
    else:
        n_arr[i] = 0    

if n_arr[N] == 1:
    print("SK")
else:
    print("CY")