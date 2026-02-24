import sys
input = sys.stdin.readline 

T = int(input())
for _ in range(T):
    S, E = map(int, input().split())
    nums = [0] * (2**31 + 1)
    
    
#짝수일떄와 홀수일때 뭐가 다르지?
# 15 => 1 2  
# 16 => 1 2 3 4 3 2   