import sys
from collections import defaultdict, deque
input = sys.stdin.readline 

#dict로 dict[사람] = [파티번호들]
#파티번호에 해당하는 곳만 다시 큐에 넣기 

dict = defaultdict(list)
N, M = map(int, input().split())
truth = list(map(int, input().split()))

t_set = set()
partys = [[] for _ in range(M)]
party_true = [0]*M 
for i, member in enumerate(truth):
    if i != 0:
        t_set.add(member)

for i in range(M):
    temp = list(map(int, input().split()))
    
    for member in temp[1:]:
        dict[member].append(i)
        partys[i].append(member)
    
# print(t_set)
# print(dict)

q = deque()
for m in t_set:
    q.append(m)
    
while q:
    m = q.popleft()
    for p_i in dict[m]:
        party_true[p_i] = 1
        for other in partys[p_i]: 
            if other not in t_set:
                q.append(other)
                t_set.add(other)

print(M - sum(party_true))