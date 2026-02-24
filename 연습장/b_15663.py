import sys
input = sys.stdin.readline 

def dfs(depth):
    if depth == M:
        tup = tuple(result)
        if tup not in result_set:
            print(" ".join(map(str, tup)))
            result_set.add(tup)
        return
    for i, num in enumerate(nlist):
        if visited[i] == 0:
            visited[i] = 1
            result.append(num)
            dfs(depth + 1)
            visited[i] = 0 
            result.pop()
        
N, M = map(int, input().split())
nlist = list(map(int, input().split()))
nlist.sort()
visited = [0] * len(nlist) 
result = []
result_set = set()

dfs(0)