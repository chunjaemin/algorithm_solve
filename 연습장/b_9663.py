import sys 
input = sys.stdin.readline 

N = int(input())

ans = 0 
col = [0]*N
diag1 = [0]*(2*N -1)
diag2 = [0]*(2*N - 1) 

def nqueen(row):
    global ans 
    if row == N:
        ans += 1 
        return 
    for c in range(N):
        if col[c] == 0 and diag1[row - c + N - 1] == 0 and diag2[row + c] == 0:
            col[c] = 1
            diag1[row - c + N - 1] = 1
            diag2[row + c] = 1
            nqueen(row +1)
            col[c] = 0
            diag1[row - c + N - 1] = 0
            diag2[row + c] = 0
            
nqueen(0)
print(ans)