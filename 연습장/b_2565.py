import sys
input = sys.stdin.readline 

N = int(input())

#왼쪽 숫자 기준으로 오른차순 정렬 후 오른쪽 수 배열에 담기
#배열의 길이 - lis 길이 = 정답  
pair_arr = []
for i in range(N):
    a, b = map(int, input().split())
    pair_arr.append((a,b))

pair_arr.sort()
nums = []
for a, b in pair_arr:
    nums.append(b)

# print(nums)

N = len(nums)
dp = [1] * N

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))