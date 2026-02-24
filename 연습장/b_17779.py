import sys
input= sys.stdin.readline 

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

ans = sys.maxsize 
for x in range(N):
    for y in range(N):
        for d1 in range(1,N):
            for d2 in range(1,N):
                if x + d1 >= N or x + d2 >=N  or y - d1 < 0 or y + d2 >= N or x + d1 + d2 >= N or y + d2 -d1 < 0 or y+d2-d1 >= N:
                    continue
                T1, T2, T3, T4, T5 = 0,0,0,0,0
                
                min_d = min(d1, d2)
                for i in range(min_d):
                    T5 += (d1 - i) * (d2 - i)
                
                T1 += x * y 
                for i in range(d1+1):
                    T1 += y - i
                
                T2 +=  (N-1-x) * (y - d1)
                for i in range(d2+1):
                    T2 += N - 1 - (x + d1 + i)
                
                T3 += ((N - 1) - (y + d2)) * (x + d2)
                for i in range(d2+1):
                    T3 += x + i 
                
                T4 += (N-1 - (x+d1+d2)) * (N-1 - (y-d1+d2))
                for i in range(d1+1):
                    T4 += N -1 - (y + d2 - i)
                
                print(x,y,d1,d2)
                print("개별:","T1", T1,"T2",T2,"T3",T3,"T4",T4,"T5",T5)
                print("합:",T1 + T2 + T3 + T4 + T5)
                max_T = max(T1,T2,T3,T4,T5)
                min_T = min(T1,T2,T3,T4,T5)
                ans = min(ans, max_T - min_T)
print(ans)