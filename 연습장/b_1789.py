import sys
input = sys.stdin.readline

N = int(input())

n = 0
temp = N
while temp >= 0:
    n += 1
    temp -= n
    
print(n-1)
    