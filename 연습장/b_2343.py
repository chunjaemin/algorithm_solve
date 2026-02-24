import sys
input = sys.stdin.readline 

N, M = map(int, input().split())
nums = list(map(int, input().split()))

#같은길이 M개로 쪼갰을 때 최소가 되는 값 찾기 
#파라메스틱 서치아님?
#맞네 시간복잡도도 딱 nlogn으로 끊기고 

def check (x):
    used = M
    cur_r = x
    for i in range(N):
        if cur_r - nums[i] >= 0:
            cur_r -= nums[i]
        else:
            used -= 1
            cur_r = x - nums[i]
    
    if used <= 0:
        return False 
    else:
        return True  

l, r = max(nums), sum(nums)

ans = sys.maxsize 
while l<=r:
    m = (l+r) // 2
    if check(m):
        r = m-1 
        ans = min(ans, m)
    else:
        l = m+1
print(ans)