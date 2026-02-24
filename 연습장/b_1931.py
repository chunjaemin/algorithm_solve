import sys
input = sys.stdin.readline

N = int(input())

rooms = []
for i in range(N):
    s, e = map(int, input().split())
    rooms.append((s,e))
    
rooms.sort(key = lambda p : (p[1], p[0]))

# print(rooms)

ps, pe = 0, 0
cnt = 0  
for i in range(len(rooms)):
    cs, ce = rooms[i]
    if pe <= cs:
        cnt += 1
        ps, pe = cs, ce

print(cnt)