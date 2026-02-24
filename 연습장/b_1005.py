import sys
from collections import deque 
input = sys.stdin.readline 

#cost 배열을 하나 만들어서 관리??
#자신에게 도착했을 때 까지의 최대 값을 cost에 저장해야됨, 그것을 기준으로 계속 확장??
#그리디는 아닌가?, 최대값 다익스트라인가? 
#이거 최대값 크루스칼 아님?
#"거쳐가야 하는" 노드의 모든 간선을 다써야함 => 다시말해 가장 큰 길은 무조건 써야됨
#최소값을 찾으라는데 애초에 최소값이 아니라 항상 고정값 아님? ?? 고정값에 최소를 구하라는게 말이되나 내가 문제 이해를 잘 못한건가 일단 풀어

#잠깐만 크루스칼 안되는거 같은데??
#크루스칼 만들었을 때가 답과 연관되어있는건 맞음
#근데 필요없는 곁가지들이 생김, 이 곁가지 제거할 수 있음? | 어떻게 구분할건데 
#별도의 cost배열을 같이둬서 크루스칼 연결할때마다 => 말안됨 걍 bfs가 맞는 듯 


T =int(input())

for _ in range(T):
    N, K = map(int, input().split())
    times = list(map(int, input().split()))
    times = [0] + times
    cost = [times[i] for i in range(N+1)]
    g = [[] for _ in range(N+1)]
    indeg = [0] * (N+1)
    
    for i in range(K):
        a, b = map(int, input().split())
        g[a].append(b)
        indeg[b] += 1 
    
    E = int(input())

    q = deque()
    for i in range(1, N+1):
        if indeg[i] == 0:
            q.append(i)
    
    while q:
        x = q.popleft()
        
        for nx in g[x]:
            cost[nx] = max(cost[nx], cost[x] + times[nx])
            indeg[nx] -= 1
            
            if indeg[nx] == 0:
                q.append(nx)  
    
    print(cost[E])

