import sys
input = sys.stdin.readline 

T = int(input())


for t in range(T):
    ans = 0 
    students = list(map(int, input().split()))
    students.pop(0)
    # print(students)
    sorted_st = [students[0]]
    for i in range(1, len(students)):
        min_j = sys.maxsize
        for j in range(len(sorted_st)):
            if sorted_st[j] > students[i]:
                min_j = min(min_j, j)
        
        if min_j == sys.maxsize:
            min_j = len(sorted_st)
        ans += len(sorted_st) - min_j
        sorted_st.insert(min_j, students[i])
    print(t+1, ans)