import sys
input = sys.stdin.readline  

N, M = map(int, input().split())

possible = [1]*(M+1)
for _ in range(N):
    K = int(input())
    nums = list(map(int, input().split()))
    get_items = 0 
    for x in nums:
        if possible[x] == 1:
            possible[x] = 0
            get_items = 1
            print(x)
            break
    
    if get_items == 0:
        print(0)

    
    
