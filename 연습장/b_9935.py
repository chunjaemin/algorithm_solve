import sys
input = sys.stdin.readline 

S =list(input().rstrip())
T = list(input().rstrip())

pt = 0 
sq = []
for pt in range(len(S)):
    sq.append(S[pt]) 
    if len(sq) >= len(T):
        if sq[len(sq) - len(T):] == T:
            # print(sq)
            del sq[len(sq) - len(T):]
            # print(sq)

if sq == []:
    print("FRULA")
else:    
    print("".join(sq))
# print(S)
# print(T)

