import sys
input = sys.stdin.readline

N, K = map(int, input().split())
houses = sorted(int(input()) for _ in range(N))

def check(mid):
    cnt = 1
    last = houses[0]

    # 첫 집은 이미 선택했으니 1번 인덱스부터
    for x in houses[1:]:
        if x - last >= mid:
            cnt += 1
            last = x
            if cnt == K:   # 더 볼 필요 없음
                return True
    return cnt >= K

# 가능한 최대 간격 = 가장 오른쪽 집 - 가장 왼쪽 집
left, right = 1, houses[-1] - houses[0]
answer = 0

while left <= right:
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)
