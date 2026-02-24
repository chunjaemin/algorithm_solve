import sys
input = sys.stdin.readline

N = int(input())
score = [list(map(int, input().split) for _ in range(N))]

#n!은 안되고, dp 같음

#상태정의는 어떻게 할거임? dp[i][j]?
#i번째 사람까지 고려했을 떄 => n개의 물건중 누가 누구를 담당했는지 모름 

#