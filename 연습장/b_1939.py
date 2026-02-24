import sys
import heapq   
input = sys.stdin.readline 

#문제만 보면 최대유량 문제 같은데, 최대유량 알고리즘을 모름
#모르는 상태로 풀 수 있나?, 1~n으로 이어지는 모든 경로에 대해 지나간 간선 중 최소값을 나타내면 되는데 
#DFS로 풀었을 때도 n^2만 되도 안되고
#DP는 어떰? 다익스트라처럼 하되 그리디는 빼고 가능? 시간복잡도에 안걸리나 
#시간복잡도는 되는거 같음 다만, 큐에 넣는과정에서 재방문을 허용하면서도 무한루프에 빠지지 않도록 해야됨
#값을 갱신 시키지 못하는 애들은 큐에 안넣는 방식으로 하면 될 것 같은데?? 

#이게 다익스트라로 풀리네, 얘도 결국 마지막 if문 보면 nw > mv[nx] 일때 갱신하는 걸 볼 수 있음
#이걸 잘 생각해보면 결론적으로 nw가 큰 놈들이 작은놈들보다 "우선순위"가 높다는거임
#이걸 기반으로 다익스트라로 풀 수도 있겠구나 하는 생각으로 이어나갈 수 있는 것 같음 
#다익스트라 => c,x 꼴이라는걸 이해하고, if문으로 가지치기 할 수 있음을 알아야됨
#가지치기가 핵심인데, 넣기직전에 mv[nx] = nw를 해주었기 때문에, 그전에 누가 갱신한게 아니면 c == mv[x]여야함
#다시말해 c != mv[x]라면(갱신시킨 것이라면), c < mv[x] 상태일 것임, 그래서 이상태면 가지치기를함 더 좋은애가 다녀간 것이니까 

#MST로도 풀린다는데 그것도 공부해봐야 할 듯 

def mflow(s, e):
    hq = [] 
    mv = [0] * (N+1) #초기화 부분이 좀 문제네 각 나가는 간선들보다는 값이 커야되면서 들어오는 간선보다는 값이 작아야한다고?  
    mv[s] = sys.maxsize #초기화 부분도 시작점만 크게 처리하고 나머지 작게 처리하면 윗줄에 적은 초기화 과정에서 생기는 모순을 해결 가능함
    
    heapq.heappush(hq, (-sys.maxsize, s))
    
    while hq:
        c, x = heapq.heappop(hq)
        c = -c 
        # print(c, mv[x])
        if mv[x] > c:
            continue 
            
        for nw, nx in g[x]:
            nw = min(nw, c)
            # print(nw, mv[nx])
            if nw > mv[nx]:
                mv[nx] = nw
                heapq.heappush(hq, (-nw, nx))
    # print(mv)
    return mv[e]

N, M = map(int, input().split())
g = [[] for _ in range(N+1)]

for i in range(M):
    a, b, w = map(int, input().split())
    g[a].append((w, b))
    g[b].append((w, a))

S, E = map(int, input().split())
print(mflow(S,E))

# print(g)    
# print(S, E)