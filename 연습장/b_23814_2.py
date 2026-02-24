import sys
input = sys.stdin.readline 

# 부족한1 + 부족한 2 = > 0 ~ 2*(D - 1) 범위 | 부족한3 => 0~ D-1 범위, 
# 케이스 1 =>  부족한1 + 부족한2 <= 부족한3 => 해줘야함 
# 케이스 2 =>  부족한1 + 부족한2 > 부족한3 and 부족한1 <= 부족한3 or 부족한2 <= 부족한3  => 부족한3으로만 나눠주기
# 케이스 3 =>  부족한1 + 부족한2 > 부족한3 and 부족한 둘다 > 부족한3 and 부족한1 + 부족한2 <= D + r_k => 부족한 1과 2한테 나눠주기 
# 케이스 4 =>  부족한1 + 부족한2 > 부족한3 and 부족한 둘다 > 부족한3 and 부족한1 + 부족한2 > D + r_k => 안나눠주기 

# => 이거 if else문으로 비교하는게 굉장히 까다로움, 논리규칙짜기도 어렵고
# GPT 말로는 복잡하게 if else문 하지말고 그냥 4개다 한번 해보고 제일 큰놈 고르라고 함 
# 시간복잡도는 미세하게 나쁠지 몰라도 별차이도 없고 좋은 듯 

D = int(input())
N, M, K = map(int, input().split())

r_n = (D - N % D) % D 
r_m = (D - M % D) % D
r_k = K % D

R = [(r_n, r_m), (0, r_m), (r_n, 0), (0, 0)] #어차피 이 4개중 하나를 하게 될 것이기에 다해봄

mandu_cnt = 0 
bob = 0 
for do_n, do_m in R:
    temp_cnt =  (N + do_n) // D + (M + do_m) // D + (K  - (do_n + do_m)) // D 
    # print(do_n, do_m, temp_cnt)
    if mandu_cnt < temp_cnt:
        mandu_cnt = temp_cnt
        bob = K  - (do_n + do_m)
    elif mandu_cnt == temp_cnt:
        if bob < K  - (do_n + do_m):
            mandu_cnt = temp_cnt
            bob = K  - (do_n + do_m)

print(bob)