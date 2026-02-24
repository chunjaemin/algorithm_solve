import sys
input = sys.stdin.readline

N = int(input())
lines = [tuple(map(int, input().split())) for _ in range(N)]

# 1. 정렬
lines.sort()

# 2. 초기값: 첫 번째 선분을 기준으로 설정
# 이렇게 하면 te = 0 문제나 -sys.maxsize 같은 고민이 사라집니다.
current_start = lines[0][0]
current_end = lines[0][1]
ans = 0

# 3. 두 번째 선분부터 순회
for i in range(1, N):
    next_start, next_end = lines[i]
    
    # [Case 1] 겹치거나 이어지는 경우 (선분 확장)
    if next_start <= current_end:
        current_end = max(current_end, next_end)
        
    # [Case 2] 완전히 끊어진 경우 (정산 및 새 시작)
    else:
        ans += (current_end - current_start) # 지금까지 이어진 길이 더하기
        current_start = next_start           # 새로운 시작점
        current_end = next_end               # 새로운 끝점

# 4. 루프가 끝나고 남은 마지막 선분 처리 (중요!)
ans += (current_end - current_start)

print(ans)