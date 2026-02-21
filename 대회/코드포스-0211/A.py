import sys
input = sys.stdin.readline

#답은 0 or 10만 가능 하다 
#다시말해 x가 존재할 수 있는 놈인지 구분만 할 수 있으면 된다. 
#그리고 x는 9의 배수로만 존재 가능하다. 즉 9의 배수인지만 알면 된다. 

def check(x):
    nums = list(map(int, list(str(x))))
    return x - sum(nums) == N 

T = int(input())
for i in range(T):
    N = int(input())
    chk = 0
    for i in range(N, N+101):
        if check(i):
            chk = 1 

    if chk == 1:
        print(10)
    else:
        print(0)