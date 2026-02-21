import sys
from collections import Counter

def custom_sort(arr):
    # 0은 제외하고 카운트
    n_cnt = Counter([x for x in arr if x != 0])
    # (횟수, 숫자) 순으로 정렬해야 '횟수'가 우선순위가 됨
    temp = sorted(n_cnt.items(), key=lambda x: (x[1], x[0]))
    
    res = []
    for num, count in temp:
        res.extend([num, count])
    # 최대 100개까지만 유지
    return res[:100]

def solve():
    R, C, K = map(int, sys.stdin.readline().split())
    R, C = R - 1, C - 1  # 0-indexed
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]

    for time in range(101):
        # 현재 배열 크기가 R, C를 포함하는지 확인 후 K값 체크
        if R < len(A) and C < len(A[0]):
            if A[R][C] == K:
                print(time)
                return

        new_A = []
        max_l = 0
        
        if len(A) >= len(A[0]):  # R 연산 (행 정렬)
            for row in A:
                sorted_row = custom_sort(row)
                new_A.append(sorted_row)
                max_l = max(max_l, len(sorted_row))
            
            # 패딩 작업
            for i in range(len(new_A)):
                new_A[i] += [0] * (max_l - len(new_A[i]))
            A = new_A
            
        else:  # C 연산 (열 정렬)
            # 열을 행으로 변환하여 처리하기 위해 zip 사용
            for col in zip(*A):
                sorted_col = custom_sort(list(col))
                new_A.append(sorted_col)
                max_l = max(max_l, len(sorted_col))
            
            # 패딩 작업
            for i in range(len(new_A)):
                new_A[i] += [0] * (max_l - len(new_A[i]))
            
            # 다시 행과 열을 뒤집어서 원래 구조로 복구
            A = list(map(list, zip(*new_A)))

    print(-1)

solve()