import sys
input = sys.stdin.readline

def dfs(depth):
    if depth == M:
        tup = tuple(result)
        if tup not in nset:
            print(" ".join(map(str, result)))
            nset.add(tup)
        return 
    for num in nums:
        if len(result) == 0:
            result.append(num)
            dfs(depth+1)
            result.pop()
        else:
            if result[-1] <= num:
                result.append(num)
                dfs(depth+1)
                result.pop()
                
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
result = []
nset = set()

dfs(0)