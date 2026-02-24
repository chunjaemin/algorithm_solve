import sys
input = sys.stdin.readline

N = int(input())
n_nums = list(map(int, input().split()))
n_nums.sort()
M = int(input())
m_nums = list(map(int, input().split()))

def binary_search(arr, x):
    l, r = 0, len(arr) - 1
    while l <= r:
        mid = (l+r) // 2
        if arr[mid] < x:
            l = mid+1
        elif arr[mid] > x:
            r = mid-1
        else:
            return 1 
    return 0 

for x in m_nums:
    print(binary_search(n_nums, x))