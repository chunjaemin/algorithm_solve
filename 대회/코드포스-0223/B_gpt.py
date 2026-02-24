import sys

def solve():
    # 터미널에서 한 줄씩 입력받기 위해 readline 사용
    line = sys.stdin.readline()
    if not line:
        return
    t_cases = int(line.strip())

    for _ in range(t_cases):
        n_line = sys.stdin.readline()
        if not n_line:
            break
        n = int(n_line.strip())
        x = sys.stdin.readline().strip()
        
        def get_t(idx):
            return 'a' if idx % 2 == 1 else 'b'

        # dp[l]: 현재 단계에서 가능한 왼쪽 사용 개수 l의 집합
        # n이 20만이라서 집합을 다 들고 있으면 느림 -> 구간(range)으로 관리
        # 하지만 홀수 l과 짝수 l의 범위가 다를 수 있으므로 각각 관리
        
        # current_possibilities: {l_value}
        # 초기 상태: 왼쪽에서 0개 사용함
        current_l = {0}

        possible = True
        for i in range(1, n + 1):
            char_x = x[i-1]
            next_l = set()
            
            # i번째 글자를 선택할 때 가능한 l들에 대하여
            for l in current_l:
                # 1. 왼쪽에서 가져오기 (l+1 번째 글자)
                if char_x == '?' or get_t(l + 1) == char_x:
                    next_l.add(l + 1)
                
                # 2. 오른쪽에서 가져오기 (r 번째 글자)
                r = n - (i - 1 - l)
                if char_x == '?' or get_t(r) == char_x:
                    next_l.add(l)
            
            # [최적화] 집합의 크기가 커지면 느려지므로, 
            # 각 홀수/짝수별로 최솟값과 최댓값만 남김 (최대 4개)
            if len(next_l) > 10:
                evens = [v for v in next_l if v % 2 == 0]
                odds = [v for v in next_l if v % 2 == 1]
                new_set = set()
                if evens:
                    new_set.add(min(evens))
                    new_set.add(max(evens))
                if odds:
                    new_set.add(min(odds))
                    new_set.add(max(odds))
                next_l = new_set

            if not next_l:
                possible = False
                break
            current_l = next_l

        print("YES" if possible else "NO")

if __name__ == "__main__":
    solve()