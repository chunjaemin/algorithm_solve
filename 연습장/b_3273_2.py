import sys
input = sys.stdin.readline

N = int(input())

nums = list(map(int, input().split()))
K = int(input())

nums_set = set()
for i in nums:
    nums_set.add(i)
    
cnt = 0 
for i in nums:
    if K - i in nums_set:
        cnt += 1

print(cnt // 2)
    