import sys
from collections import defaultdict
input = sys.stdin.readline 

# 단서1: 순열이다
# 단서2: 아랫 배열의 구간에 해당하는 수가 윗배열 구간에 존재해야한다. 
# 단서3: 아랫 배열에서 동일한 수의 구간이 1번이상 나올 수는 없다.  
# 단서4: 윗배열에서 복사되는 수는 아랫배열에 없어야 한다. 
# 아이씨 o(n)이 되네 n은 20만이라고 보면되고, nlogn까지도 노려볼만하다 할만하지 이럼 
# 바로 위만 같으면 되는줄 알았는데 대각선도 되네 지금보니까 

T = int(input())
for _ in range(T):
    N = int(input())
    nums1 = list(map(int, input().split()))
    nums2 = list(map(int, input().split()))

    if nums1[0] == nums2[0]:
        prev = 1
    else:
        prev = 0 

    candidate = [] 
    ndict = defaultdict(int)
    ndict[nums2[0]] += 1 

    ans = "Yes"
    no_ans = 0
    for i in range(1, N):
        if nums2[i-1] != nums2[i]: # 구간이 변했을 경우 
            print(i-1, i, nums2[i-1], nums2[i])
            if ndict[nums2[i]] != 0:
                ans = "No"
                no_ans = 1
                break 
            ndict[nums2[i]] += 1
            candidate.append(prev)
            prev = 0

            if nums1[i] == nums2[i]:
                prev = 1 
        else: #같은 구간일 경우 
            if nums1[i] == nums2[i]: #이 구간은 합격 
                prev = 1 

    print(candidate)
    if no_ans == 0:
        for x in candidate:
            if x == 0:
                ans = "No"    
    print(ans)