import sys
from collections import deque 
input = sys.stdin.readline 

V = int(input())
g = [[] for _ in range(V+1)]

for _ in range(V):
    nums = list(map(int, input().split()))
    i = nums[0]
    for x in range(1, len(nums) - 1, 2):
        g[i].append((nums[x], nums[x+1])) #노드번호, 가중치 
        g[nums[x]].append((i, nums[x+1]))

# print(g)

def bfs(s):
    visited = [0]*(V+1)
    q = deque()
    q.append((0, s))
    visited[s] = 1

    ans = 0 
    ans_n = -1  
    while q: 
        w, n = q.popleft()
        
        if w > ans:
            ans = w 
            ans_n = n 
        
        # print(g[n])
        for nn, nw in g[n]:
            # print(nn)
            if visited[nn] == 0:
                visited[nn] = 1 
                q.append((w + nw, nn))
    return [ans_n, ans] 

final_point1, dist1 = bfs(1)
final_point2, dist2 = bfs(final_point1)

print(dist2)
