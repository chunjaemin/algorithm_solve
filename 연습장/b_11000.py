import sys
input = sys.stdin.readline 
import heapq 

rooms = []
ends = []

N = int(input())

for i in range(N):
    s, e = map(int, input().split())
    rooms.append((s,e))
    
rooms.sort(key = lambda p : (p[0], p[1]))

e = 0
cnt = 1
heapq.heappush(ends, 0)
for room in rooms:
    cs, ce = room
    e = ends[0]
    if e > cs:
        cnt += 1
    else:
        heapq.heappop(ends) 
    heapq.heappush(ends, ce)
    
print(cnt)