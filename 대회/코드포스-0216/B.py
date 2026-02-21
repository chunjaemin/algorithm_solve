import sys
input = sys.stdin.readline 

#이어져 있는 칸들?? 1,2,4,8,16...
# 3,6,12,24

#안될 수 밖에 없는 조건이 있지않을까? 

#모든 집단은 버블정렬로 정렬가능 => 같은 집단 내에선 위치교환 얼마든지 가능 
#순열이잖아 => 각 숫자는 자기가 있어야할 자리가 정해져 있지 
#특정 숫자를 봤다 => 얘가 있어야할 위치를안다 => 즉시 배수로 검사해서 판단할 수 있다. 


T = int(input())

for _ in range(T):
    N = int(input())
    nums= [0] + list(map(int, input().split()))
    
    ans = 1
    for i in range(1, N+1):
        idx = i #1베이스 인덱스 
        check = 0 #처음엔 0, 하나라도 자리 찾으면 1 
        while idx < N+1:
            # print(nums[i], idx)
            if nums[i] == idx:
                check = 1
                break
            idx *= 2
        
        if check == 1:
            continue 
            
        idx = i #1베이스 인덱스 
        check = 0 #처음엔 0, 하나라도 자리 찾으면 1 
        while True:
            # print(nums[i], idx)
            if nums[i] == idx:
                check = 1
                break
            if idx % 2 == 0:
                idx = idx // 2
            else:
                break     
            
        if check == 0:
            ans = 0 
            break 
    if ans == 1:
        print("YES")
    else: 
        print("NO")