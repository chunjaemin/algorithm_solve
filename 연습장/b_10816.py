import sys
from bisect import bisect_left, bisect_right
input = sys.stdin.readline

N = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()
M = int(input())
m_arr = list(map(int, input().split()))

ans = list()
for x in m_arr:
    print(bisect_right(n_arr,x) - bisect_left(n_arr,x), end=' ')
