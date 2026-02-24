import sys
input = sys.stdin.readline 

def dfs(depth, nums, path):
    if depth == M:
        print(" ".join(map(str, path)))
        return 
    for i in nums:
        next_nums = [x for x in nums if x != i]
        next_path = path + [i]
        dfs(depth+1, next_nums, next_path)

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

dfs(0, nums,[])