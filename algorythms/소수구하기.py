def get_prime(n):
    p = [1] * (n+1)
    p[0], p[1] = 0 #0과 1은 소수가 아님 
    for i in range(2, int(n**.5) + 1):
        for j in range(i*i, n+1, i): #i를 제외한(i보다 큰) i의 배수 모두 지우기 
            p[j] = 0
    return [i for i in range(n + 1) if p[i]]

print(get_prime(30))

# 2부터 N까지의 모든 수를 나열합니다.
# 아직 지워지지 않은 수 중 가장 작은 수 P를 찾습니다 (이것은 소수입니다).
# P를 제외한 P의 배수들을 모두 지웁니다.
# 더 이상 반복할 수 없을 때까지 2~3번을 반복합니다.