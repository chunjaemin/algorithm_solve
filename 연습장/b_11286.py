import sys
import heapq
input = sys.stdin.readline 

N = int(input())

hq = []
 
for i in range(N):
    n = int(input())
    if n != 0:
        v = (max(n, -n), n)
        heapq.heappush(hq, v)
    else:
        if len(hq) != 0:
            v = heapq.heappop(hq)
            print(v[1])
        else:
            print(0)
        