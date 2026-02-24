import sys
input =sys.stdin.readline 

#출발점과 도착점 사이에 몇개의 원이 존재하는가? 
#특정 원이 출발점과 도착점 => 둘중 하나는 포함하고 하나는 포함하지 않을 때 반드시 지나가야 함 
#특정 원이 둘다 포함하거나 둘다 포함하지 않을 경우 피해서 갈 수 있음 
#모든 원에 대해 포함관계를 조사하면 될 듯 

T = int(input())

for _ in range(T):
    sx,sy,ex,ey = map(int, input().split())
    N = int(input())
    ans = 0
        
    for i in range(N):
        x, y, r = map(int, input().split())
        # print("거리: ", (sx - x)**2 + (sy- y)**2)
        if (sx - x)**2 + (sy- y)**2 < r*r: 
            in_s = 1
        else:
            in_s = 0
        
        if (ex - x)**2 + (ey- y)**2 < r*r: 
            in_e = 1
        else:
            in_e = 0
        
        if in_s + in_e == 1:
            # print("포함: ",x, y, r)
            ans += 1 
    print(ans)