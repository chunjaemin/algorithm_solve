import sys
input = sys.stdin.readline

def check(mid):
    cnt = 0 
    for i in range(K): #피드백, range(K)말고 lines로 원소 가져오는 for문이 더 좋음  
        cnt += lines[i] // mid
    return cnt >= N 


K, N = map(int, input().split())

lines = [int(input()) for _ in range(K)]
l, r = 1, max(lines)

answer = 0
while l<=r:
    mid = (l+r) // 2
    if check(mid):
        answer = mid
        l = mid + 1
    else:
        r = mid - 1

print(answer)