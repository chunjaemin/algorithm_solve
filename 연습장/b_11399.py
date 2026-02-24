import sys
input = sys.stdin.readline 

N = int(input())
nums = list(map(int, input().split()))

nums.sort()

ans = 0 

for i,num in enumerate(nums):
    ans += sum(nums[:i+1])

print(ans)