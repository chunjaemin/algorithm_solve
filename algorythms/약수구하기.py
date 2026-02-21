#아이디어: n = a * b 꼴임, a를 구하면 b도 확정 되는 것을 이용하여 추가함(n = a*a 일 수도 있으니 중복추가 방지해서 구현)
def get_divisors(n):
    divisors = []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:  # 제곱근일 경우 중복 추가 방지
                divisors.append(n // i)
    return sorted(divisors)

print(get_divisors(36)) # [1, 2, 3, 4, 6, 9, 12, 18, 36]


#위와 같은 코드. 더 쓰기 편한 형태 
def get_divs(n):
    res = set()
    for i in range(1, int(n**0.5)+1):
        if i % n == 0:
            res.add(i)
            res.add(n//i)
    return sorted(res)