import sys
input = sys.stdin.readline 

s = list(input().rstrip())

idx = 0 
zero = True  
for i in range(len(s)):
    if s[i] == 'x':
        idx = i
        zero = False  
        break 

if zero:
    print(0)
    exit()

if idx == 0:
    print(1)
    exit()

nums = []
for i in range(0, idx):
    nums.append(s[i])

ss = ''
for x in nums:
    ss += x 

if ss == '-':
    print('-1')
    exit()
print(int(ss))