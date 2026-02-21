import sys
input =sys.stdin.readline 

#n개의 방정식  & n개의 미지수 => 답을 구할 수 있음
#일반적으로 이건 I를 만드는 선형대수학 행렬임 
#

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    