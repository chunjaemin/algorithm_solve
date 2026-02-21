import sys
input = sys.stdin.readline 

def get_prime(n):
    p = [1] *(n+1)
    p[0], p[1] = 0, 0
    for i in range(2, int(n**0.5)+1):
        for j in range(i*i, n+1, i):
            p[j] = 0
    return [i for i in range(n+1) if p[i]]

N, M = map(int, input().split())

ps = get_prime(M)
for x in ps:
    if x >= N:
        print(x)