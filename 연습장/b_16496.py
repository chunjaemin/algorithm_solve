import sys
input = sys.stdin.readline 

N = int(input())

nums = input().split()
nums.sort(key = lambda x : x*10, reverse = True)
print(str(int(''.join(nums))))
