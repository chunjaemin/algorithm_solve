import sys
from collections import defaultdict
input = sys.stdin.readline

#배낭문제로 환원 되는 문제
#묶음을 어떻게 만들 수 있지? | union으로 묶고 부모인덱스에 값들 다 넣어두기? 

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    pa, pb = find(a), find(b)
    
    if pa != pb:
        parent[pa] = pb 

N, M, K = map(int, input().split())

v = list(map(int, input().split()))
parent = [x for x in range(N+1)]

for i in range(M):
    a, b = map(int, input().split()) 
    union(a, b)

V_map, W_map = defaultdict(int), defaultdict(int) 

for x in range(1, N+1):
    px = find(x)
    V_map[px] += v[x-1]
    W_map[px] += 1

W, V = [0], [0]
for k in V_map.keys():
    V.append(V_map[k]) 
    W.append(W_map[k]) 
    
    
N = len(V) -1 
dp = [[0] * (N+1) for _ in range(K)]

# dp[1][W[1]] = V[1]
# print(dp)

for i in range(1,K): #무게 
    for j in range(1,N+1): #아이템 인덱스
        if i - W[j] >= 0: 
            dp[i][j] = max(dp[i][j-1], dp[i - W[j]][j-1] + V[j])
        else:
            # print(dp[i][j], dp[i-1][j])
            dp[i][j] =  dp[i][j-1]

# print(dp)
print(dp[K-1][N])