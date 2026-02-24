import sys
from collections import deque  
input = sys.stdin.readline 

#봄 여름 가을 겨울 4가지가 한턴 
#봄 => 양분 먹기, 두개이상 => 어린놈 부터  | 못먹으면 즉시죽음
#여름 => 죽은놈은 나이의 절반이 양분이 됨
#가을 => 번식 5의 배수인 애들 주변에 나무추가 
#겨울 => 양분 뿌리기 (A배열 값 그대로 추가)

R = [-1,0,1,-1,1,-1,0,1]
C = [-1,-1,-1,0,0,1,1,1]
N, M, K = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]

energy = [[5] * N for _ in range(N)]
trees = [[deque() for _ in range(N)] for _ in range(N)]

for i in range(M): #(나이, 생존여부)
    r, c, age = map(int, input().split())
    trees[r-1][c-1].append(age) 

def spring ():
    for r in range(N):
        for c in range(N):
            stored_tree = deque()
            stored_energy = 0 
            for i in range(len(trees[r][c])):
                age = trees[r][c].popleft()
                if age <= energy[r][c]:
                    energy[r][c] -= age 
                    stored_tree.append(age+1) 
                else:
                    stored_energy += age // 2
            trees[r][c] = stored_tree 
            energy[r][c] += stored_energy

def fall():
    for r in range(N):
        for c in range(N):
            for i, age in enumerate(trees[r][c]):
                if age % 5 == 0:
                    for i in range(len(R)):
                        nr = r + R[i]
                        nc = c + C[i]
                        if 0<= nr < N and 0 <= nc < N:
                            trees[nr][nc].appendleft(1)

def winter():
    for r in range(N):
        for c in range(N):
            energy[r][c] += A[r][c]

def cnt_alive():
    ans = 0
    for r in range(N):
        for c in range(N):
            for i, tree in enumerate(trees[r][c]):
                # print(tree)
                ans += 1 
    #             print(i, tree, ans)
    # print("ans", ans)
    return ans 

for t in range(K):
    spring()
    # summer()
    fall()
    winter()
print(cnt_alive())

# for row in trees:
#     for tree in row:
#         print(tree)

# for row in energy:
#     print(" ".join(map(str, row)))
         
