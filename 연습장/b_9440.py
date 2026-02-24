import sys
input = sys.stdin.readline 

#개수 반으로 쪼갬
# case1 = n,n     | n은 오름차순이어야함 +  
# case2 = n, n+1  | 
#오름차순 정렬하고 좌우 하나씩 넣어주면 되지않음? 맞는 듯 
#그리디 문제네  
#정렬 후 0 따로처리, 나머지는 바로 정답에 10*(n -i)로 곱해서 더해주기
#0 처리가 까다로운 듯 0은 항상 n-1자리수로 곱해서 더해주면 될 듯?
#0처리 숫자로 하면 개 빡쌔네 그냥 배열 두개로 나눠서 저장하는게 훨씬 편할 듯 

while True:
    ans = 0 
    nums = list(map(int, input().split()))
    N = len(nums) - 1
    
    if N == 0 and nums[0] == 0:
        break 
    nums = nums[1:]
    
    nums.sort()
    arr1 = []
    arr2 = []
    
    for i in range(N):
        if nums[i] != 0:
            nums[0], nums[i] = nums[i], nums[0]
            break
        
    for i in range(1, N):
        if nums[i] != 0:
            nums[1], nums[i] = nums[i], nums[1]
            break
    
    for i in range(N):
        if i % 2 == 0:
            arr1.append(nums[i])
        else:
            arr2.append(nums[i])

                
    arr1 = int("".join(map(str, arr1)))
    arr2 = int("".join(map(str, arr2)))
    print(arr1 + arr2)
    # print(arr1)
    # print(arr2)