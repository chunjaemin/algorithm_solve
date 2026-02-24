import sys
input = sys.stdin.readline

N = int(input())

s = set()

for i in range(N):
    temp = input().split()
    if len(temp) == 1:
        action = temp[0]
        if action == "all":
            s.update([i for i in range(1, 21)])    
        if action == "empty":
            s.clear()
    if len(temp) == 2:
        action = temp[0]
        v = int(temp[1])
    
        if action == "add":
            s.add(v)
        if action == "remove":
            s.discard(v)
        if action == "check":
            if v in s:
                print(1)
            else:
                print(0)
        if action == "toggle":
            if v in s:
                s.remove(v)
            else:
                s.add(v)
