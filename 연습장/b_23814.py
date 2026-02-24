import sys
input = sys.stdin.readline 

# r_k + D 가
# 2 2 0

# 부족한1 + 부족한 2 = > 0 ~ 2*(D - 1) 범위 | 부족한3 => 0~ D-1 범위, 
# 케이스 1 =>  부족한1 + 부족한2 <= 부족한3 => 해줘야함 
# 케이스 2 =>  부족한1 + 부족한2 > 부족한3 and 부족한1 <= 부족한3 or 부족한2 <= 부족한3  => 부족한3으로만 나눠주기
# 케이스 3 =>  부족한1 + 부족한2 > 부족한3 and 부족한 둘다 > 부족한3 and 부족한1 + 부족한2 <= D + r_k => 부족한 1과 2한테 나눠주기 
# 케이스 4 =>  부족한1 + 부족한2 > 부족한3 and 부족한 둘다 > 부족한3 and 부족한1 + 부족한2 > D + r_k => 안나눠주기 

D = int(input())
N, M, K = map(int, input().split())

r_n = (D - N % D) % D 
r_m = (D - M % D) % D
r_k = K % D

if r_n <= r_m:
    f, s = r_n, r_m 
else:
    f, s = r_m, r_n 

if f + s <= r_k:
    print(K - (f + s))
else: 
    if f <= r_k:
        print(K - f)
    else:
        if f + s <= D + r_k:
            print(K - (f + s))
        else: 
            print(K)
    