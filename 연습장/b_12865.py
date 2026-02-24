import sys
input = sys.stdin.readline 
#물건이 커서 배낭에 못 넣는 경우(w-W[i]<0인 경우) 이전dp[i][w] = dp[i-1][w]를 해주어야 하는데 안해줘서 틀렸음 조심!
 

# 무게와 가치가 있음, K무게를 넘지않으면서 가치를 최대로 해야함 

#dp[w] = > 무게 w 일 때의 최대 가치 라고 두면 어떰? 
#무게가 w 일 때 최대가 된다고 치면, 무게 w 안에 어떤 아이템이 들어있는지 알 수 없어서 점화식을 못세움

#상태정의 dp[i][w] => 물건 0~i번까지만 고려했을 때 무게 w일 때의 최대 가치  
#점화식 => dp[i][w] = max(dp[i-1][w], dp[i-1][w - W[i]] + V[i])

#dp에 도움이 되는 접근 방법론들
#1. 상태정의는 어떤 것으로 해야하는가?
#2. 점화식은 어떻게 세워야 하는가? 

#3. 굉장히 적을 때 부터 생각해보는 방식 (한 개일 때, 두개일 때)
#4, 엣지 케이스 (과하게 치중된 케이스에 대해 생각), 다양한 케이스에 대해 생각해보기 

N, K = map(int, input().split())
W, V = [0], [0]
for i in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[0] * (K+1) for _ in range(N+1)]


for i in range(1, N+1):
    for w in range(1, K+1):
        if w - W[i] >= 0:
            dp[i][w] = max(dp[i-1][w], dp[i-1][w - W[i]] + V[i])
        else:
            dp[i][w] = dp[i-1][w]

# print(W)
# print(V)
print(dp[N][K])

