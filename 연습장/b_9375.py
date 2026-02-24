import sys
from collections import defaultdict
input = sys.stdin.readline 

#같은 종류가 있을 때 경우의 수?, 아얘 안입는건 빼야함 
#수학일까, 브루트포스일까 2^30 * 100 = 시간초과, 브루트포스는 아니고 
#예제 3 * 2 - 1, 4 - 1 => 걍 공식이네  

T = int(input())
for _ in range(T):
    N = int(input())
    store = defaultdict(int)
    for i in range(N):
        a, b = input().split()
        store[b] += 1
    ans = 1
    for k, v in store.items():
        ans *= v+1
    ans -= 1
    print(ans)