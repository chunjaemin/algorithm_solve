import sys
input = sys.stdin.readline 

A, B, C = map(int, input().split())

def power(n, d):
    if d == 1:
        return n % C
    temp = power(n, d//2)
    if d % 2 == 0: 
        return temp * temp % C 
    else:
        return temp * temp * n % C 
print(power(A, B))