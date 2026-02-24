import sys
input = sys.stdin.readline 

def seive(n):
    is_prime = [1]*(n+1)
    is_prime[0] = is_prime[1] = 0 
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = 0
    return [i for i, p in enumerate(is_prime) if p]

N = int(input())
primes = seive(N)
# print(primes)
n_p = len(primes)

cnt = 0
n_sum = 0
l = 0
for r in range(n_p):
    n_sum += primes[r]
    while n_sum > N:
        n_sum -= primes[l]
        l += 1
    
    if n_sum == N:
        cnt += 1 

print(cnt)