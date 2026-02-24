import sys
input = sys.stdin.readline 

#최대 신장 트리를 구하는 문제로 치환 가능함 
#가장 큰 도로부터 일단 이어보면서 특정 두 지점이 이어졌는지 확인하면 됨
#이어졌다면 현재 놓은 도로가 이어져 있는 도로중에선 최소이며, 앞으로 쓸 도로들보단 큼이 보장됨

#병목 경로 문제라고도 불리고
#최악의 상황중 최선을 찾는 문제임! (최소값중 최대를 찾는, 최댓값 중 최소를 찾는 문제)

#추가팁: "모든 경로 병목 문제"는 크루스칼로 풀 수 있다. 
 
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa = find(a)
    pb = find(b)
    
    if pa != pb:
        parent[pa] = pb  

N, M =map(int, input().split())
parent = [x for x in range(N+1)]

g = [[] for _ in range(N+1)]
r = []
for _ in range(M):
    a, b, w = map(int, input().split())
    r.append((w, a, b))
S, E = map(int, input().split())

r.sort(key = lambda x : -x[0])

for w, a, b in r:
    union(a, b)
    if find(S) == find(E):
        print(w)
        exit()    

# print(g)