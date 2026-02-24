import sys
input = sys.stdin.readline 

N, M = map(int, input().split())

pdict = {}
npdict = {}
for i in range(N):
    name = input().rstrip()
    pdict[name] = i + 1
    npdict[i+1] = name 

for i in range(M):
    question = input().rstrip()
    if question.isdigit():
        print(npdict[int(question)])
    else:
        print(pdict[question])
        
        