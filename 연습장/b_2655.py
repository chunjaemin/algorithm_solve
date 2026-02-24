import sys
input = sys.stdin.readline 

N = int(input())

blocks = []
for i in range(N):
    a, b, c = map(int, input().split())
    blocks.append((a,b,c))

blocks.sort(key = lambda x : (-x[0], -x[1]))
# print(blocks)

dp = [x[1] for x in blocks]
dp2 = [1]*N

for i in range(N):
    for j in range(i):
        fa, fb, fc = blocks[j]
        ba, bb, bc = blocks[i]
        # print(fa,fb,fc)
        # print(ba,bb,bc)
        if fc > bc:
            if dp[i] < dp[j] + bb:
                dp[i] = dp[j] + bb
                dp2[i] = dp2[j] + 1 
        #     print("i:", i)
        #     print(dp)
        # print("for문 끝")

print(dp)
print(dp2)
print(max(dp2))
target_len = max(dp2)

result = []
for i in range(N-1, -1,-1):
    if dp2[i] == target_len and blocks[i][]:
        target_len -= 1
        result.append(i+1)
print(result)

for i in range(len(result)):
    print(result[i])