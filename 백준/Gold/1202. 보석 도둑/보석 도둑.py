import sys
from bisect import bisect_left 
# sys.setrecursionlimit(10**6)
input = sys.stdin.readline 

#가격을 최대한 =>가격 높은순으로 넣을 수 있으면 무조건 넣어야함 
#이때 가장 작은 가방부터 넣어야함 그래야 나중에 큰거 나오면 넣을 수 있을 테니 
#아이씨 아까못푼 문제랑 똑같은 문제네 
#정렬된 배열 삭제를 O(1)만에 해야함 

def find(x):
    cur = x 
    while cur != parent[cur]:
        cur = parent[cur]

    px = cur 
    cur = x 
    
    while cur != px:
        p_cur = parent[cur]
        parent[cur] = px
        cur = p_cur 
    
    return px 

def union(a,b):
    pa, pb = find(a), find(b)
    
    if pa < pb:
        parent[pa] = pb
    elif pa > pb:
        parent[pb] = pa 

N, K = map(int, input().split())
parent = [x for x in range(K+1)]

items = []
for _ in range(N):
    m, v = map(int, input().split())
    items.append((m, v))

bags = []
for _ in range(K):
    k = int(input())
    bags.append(k)

items.sort(key = lambda x : -x[1])
bags.sort()

ans = 0 
for m, v in items:
    idx = bisect_left(bags, m)
    if idx != K:
        ridx = find(idx)
        if parent[ridx] < K:
            ans += v 
            if parent[ridx] == K-1:
                parent[ridx] += 1 
            else:
                union(ridx, ridx+1)

print(ans)