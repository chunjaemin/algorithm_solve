import sys
import math 
input =sys.stdin.readline 

#1-6, 2-5, 3-4 => 두 합이 7이면 반대편 and 같은 숫자도 바꿔야 함 => 특수조건이라 칭하자
#모든수가 인접하도록 하는 최소횟수 
#마음껏 숫자 바꾸기 가능 
#특수 케이스가 있나? 그냥 인접한것들 특수조건 만족하면 연산횟수 + 1 해주면 되는거 아닌가 
# 3숫자가 특수조건이면?? xyx 꼴이겠네
# xxx도 가능하고 => 

#슬라이딩 윈도우로 끊어서 계산해야되나??
#특수조건 구간 => 원소개수 // 2 가 최소횟수임, 그리디 아니지 아니야 
#xyxyxy, xxxxxx => ceil() 하면 될 듯 

T = int(input())

for _ in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    
    ans = 0 
    l = 0 
    for r in range(1, N):
        if nums[r-1] + nums[r] == 7 or nums[r-1] == nums[r]: #특수조건 만족 
            if r == N-1:
                ans += math.ceil((r - l) / 2)
            continue
        else:
            ans += math.ceil((r - l - 1) / 2)
            l = r 
    print(ans)
    