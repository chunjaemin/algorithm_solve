import sys
import math 
input = sys.stdin.readline 

#소수이면서 팰린드롬??
#만드는 규칙과 판별하는 규칙 두가지가 다르지않나? 

#팰린드롬 수를 만들고 거기에 소수 확인규칙을 더하는 것으로 가능할까?
#최악을 가늠할 수가 없는데 

def is_pal(s):
    s = str(s)
    return s == s[::-1]

#소수 판별 쓸 때 0과 1 예외처리 생각해주어야 함! 
def is_prime(n):
    if n < 2:
        return False 
    prime = True 
    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            prime = False 
    return prime 

N = int(input())

cur = N 
while True:
    if is_pal(cur):
        if is_prime(cur):
            print(cur)
            exit()
    cur += 1 

