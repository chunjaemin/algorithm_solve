import sys
input = sys.stdin.readline 

T = int(input())

for t in range(T):
    ans = 0 
    N = int(input())
    nums = list(map(int, input().split()))
    for x in nums:
        if x == 67:
            ans = 1 
    
    if ans == 1:
        print("YES")
    else:
        print("NO")
        