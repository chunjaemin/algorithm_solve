import sys
input = sys.stdin.readline


N = int(input())
nums = list(map(int, input().split()))


mapping = [-1]*200001
mapping[0] = 0
mapping[1] = 1
mapping[2] = 11

def make_o(n):
    if mapping[n] == -1:
        mapping[n] = make_o(n-1) + 10**(n-1)
    return mapping[n]

ans = 0
for i in range(N):
    ans += make_o(nums[i])

print(mapping[:10])
print(ans)
