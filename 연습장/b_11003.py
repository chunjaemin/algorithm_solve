import sys
import heapq
input = sys.stdin.readline 

#슬라이딩 윈도우 내에서 최소값을 어떻게 찾을 건지가 관건
#how?? logN 내에는 해야할 것임 혹은 상수시간 
#D 배열 하나 만들어서 기록해두고
#최소값을 heapq로 관리한다음
#1. 슬라이딩 윈도우 이동시 빠지는 값이 heapq의 맨앞인지 확인하고 맨앞이면 제거, 아니면 그대로 냅두기
#2. 넣어지는 값 heapq에 넣은 뒤 D배열에 heapq 맨앞값 넣어주기 
#D 배열 결과가 출력 결과임 
#=> 다시생각해보니까 이러면 맨앞값은 유효하긴한데 맨앞값을 제외한 나머지 값들이 유효하지않음, 중간에 빠지는 값들은 heap에서 못빼내서 문제 생김

#턴 개념을 넣는건 어떰? 값을 기록할 당시의 턴이 현재 턴과 L - 1 이하의 차이면 슬라이딩 윈도우 안에 있는 값임을 알 수 있을 듯 
#heapq에서 뺄 떄 유효한 값인지 턴값을 통해 확인 가능할 듯 
# l값보다 t가 크거나 같으면 유효한 값인 듯 

N, L = map(int, input().split())
nums = list(map(int, input().split()))

l = 0
hq = []
D = [] 
for r in range(N):
    heapq.heappush(hq, (nums[r], r))
    if r - l >= L:
        l += 1 
        while hq[0][1] < l:
            heapq.heappop(hq)
        D.append(hq[0][0])
    else:
        D.append(hq[0][0])

print(" ".join(map(str, D)))