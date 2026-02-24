import sys
input = sys.stdin.readline 

# N 개의 수가 모두 나머지가 같도록 하는 M 찾기
#수가 커서 이분탐색은 아님, 수학적 지식을 요구하는 것일수도? 말이안되는데 
#아니네 N이 2000이구나 T값 안나와있긴한데 이분탐색이네 => 아니지 단조성이 없으니 안되지 
#와 뭐야 개어렵네 mq + r 을 이용해서 약수를 구하는 문제 | 항상 나머지 관련 수학적 문제가 좀 빡쌘데 따로 공부해야될수도 있을듯
#참고사항 gcd => O(log(제일큰수))

def gcd (a,b):
    while b:
        a, b = b, a%b
    return a 

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int ,input().split()))
    
    nums.sort()
    
    gcd_candidate = []
    for i in range(1, N):
        gcd_candidate.append(nums[i] - nums[i-1])
    
    keep = gcd(gcd_candidate[0], gcd_candidate[1])
    for i in range(2,len(gcd_candidate)):
        keep = gcd(keep, gcd_candidate[i])
    
    if keep == 0:
        print("INFINITY")
    else:
        print(keep)