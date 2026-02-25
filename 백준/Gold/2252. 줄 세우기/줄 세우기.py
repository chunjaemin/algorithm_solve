import sys
from collections import deque 
input = sys.stdin.readline 

#순서를 볼때마다 배열에 삽입해주는건 n^2이라 안될거같고
#그래프로 순서관계를 나타내고 최장길이를 찾으면 될 거 같은데??
#순서관계 => 제대로 따라가면 정답이 나오긴함, 이때 제대로 따라간다는건 최장길이로 따라가야함
#와 이게 위상정렬이라고? 생각보다 규칙이 독특한데 왜 이런 형태를 띄게 되는지 이해하는 것도 좋을 듯?

N, M = map(int, input().split())

e = [[] for _ in range(N+1)]
inde = [0] * (N+1)
for _ in range(M):
    a, b = map(int, input().split())
    #a<-b 진출 그래프 
    e[b].append(a)
    inde[a] += 1

r_ans = []
q = deque()

for i in range(1, N+1):
    if inde[i] == 0:
        r_ans.append(i)
        q.append(i)

while q:
    x = q.popleft()
    
    for nx in e[x]:
        inde[nx] -= 1
        if inde[nx] == 0:
            q.append(nx)
            r_ans.append(nx)


ans = r_ans[::-1]
print(" ".join(map(str, ans)))