import sys
input =sys.stdin.readline 

N = int(input())
sn = list(str(N))

if sn[0] == sn[1] and sn[1] == sn[2]:
    print("Yes")
else:
    print("No")