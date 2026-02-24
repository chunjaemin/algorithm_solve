import sys 
input = sys.stdin.readline

def dfs(depth, idx, num_set, path):
    if depth == 6:
        print(" ".join(map(str, path)))
        return
    for i in range(idx, len(num_set)):
        next_path = path + [num_set[i]]
        dfs(depth+1, i+1, num_set, next_path) 
        
while True:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    dfs(0,0,arr[1:],[])
    print("")
    
    
    