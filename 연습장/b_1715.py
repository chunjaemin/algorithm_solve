import sys
import heapq 
input = sys.stdin.readline 


#합쳐야 하는 총 횟수는 항상 정해져있음!
#n개 => n-1번 비교 필수임 
#합친게 누적되면서 빠르게 클 수록 기하급수적으로 커짐, 즉 최대한 작게 만들면서 합쳐야됨
#걍 정렬 시키고 두개씩 더하면 됨 
#더할때 어케 더함?, 
#더하고 계속 정렬하는건 (n-1) * nlogn임 말안됨 
#bisect로 logn끼워넣기 같은데??
#아니 바본가 heapq 사용하면 자동 정렬인데 대체왜 이걸 고민하고 있었던 거야 하 개멍청하네진짜 


N = int(input())

hq = []
for i in range(N):
    n = int(input())
    heapq.heappush(hq, n)

ans = 0 
while len(hq) > 1:
    a = heapq.heappop(hq)
    b = heapq.heappop(hq)
    ans += a+b 
    heapq.heappush(hq,a+b)

print(ans)

