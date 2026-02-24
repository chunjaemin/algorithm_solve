import sys
from collections import deque

# sys.stdin.readline은 디버깅 중 input()과 충돌할 수 있으므로 
# 실제 제출 시에만 주석 해제하거나, 디버깅 input에는 sys.stdin.readline을 쓰지 않도록 주의합니다.
# 여기서는 편의상 input을 그대로 둡니다.

# ==========================================
# [Method 1] 시각화 헬퍼 함수 (Visualizer)
# ==========================================
def print_state(day, board, visited=None, active_group=None):
    """
    현재 땅의 상태를 보기 좋게 출력합니다.
    - active_group: 방금 인구 이동이 일어난 좌표들 (강조 표시용)
    """
    print(f"\n🔎 [Day {day} 상태 확인] " + "="*30)
    for r in range(len(board)):
        line = ""
        for c in range(len(board[0])):
            val = f"{board[r][c]:^3}" # 3칸 확보 후 가운데 정렬
            
            # 현재 연합(이동 중인 곳)은 별표(*)로 강조
            if active_group and (r, c) in active_group:
                line += f"[{val}]" 
            # 방문했던 곳은 점(.) 표시 (선택 사항)
            elif visited and visited[r][c]:
                line += f" {val} "
            else:
                line += f" {val} "
        print(line)
    print("="*45)

# ==========================================
# [Main Logic]
# ==========================================

N, L, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

total_days = 0 
is_moved = True # check 변수명 변경 (의미 명확화)

# [Debug Mode] True면 단계별로 멈춰서 보여줌, False면 그냥 돎
DEBUG_MODE = True 

while is_moved:
    if DEBUG_MODE:
        # [Method 2] 단계별 제어 (Step Control)
        print_state(total_days, board)
        cmd = input(f"Next Day({total_days + 1})로 진행하려면 Enter... (q: 종료) > ")
        if cmd == 'q': break

    is_moved = False
    visited = [[0]*N for _ in range(N)]
    
    # [Fix 1] 변수명 오염 방지
    # r, c 대신 start_r, start_c로 명명하여 
    # BFS 내부의 curr_r, curr_c와 섞이는 실수 원천 차단
    for start_r in range(N):
        for start_c in range(N):
            
            # [Fix 2] 조건문 실수 방지
            # visited (리스트 자체)가 아니라 visited[start_r][start_c] (값) 체크
            if visited[start_r][start_c] == 0:
                
                # BFS 준비
                q = deque()
                q.append((start_r, start_c))
                visited[start_r][start_c] = 1
                
                alliance = [(start_r, start_c)]
                sum_population = board[start_r][start_c]
                
                while q:
                    # [Fix 1] 변수명 명확화 (cr, cc -> curr_r, curr_c)
                    curr_r, curr_c = q.popleft()
                    
                    dr = [0, 0, 1, -1]
                    dc = [1, -1, 0, 0]
                    
                    for i in range(4):
                        next_r = curr_r + dr[i]
                        next_c = curr_c + dc[i]
                        
                        # [Method 3] 범위 체크 & 조건 검증
                        if 0 <= next_r < N and 0 <= next_c < N:
                            if visited[next_r][next_c] == 0:
                                diff = abs(board[curr_r][curr_c] - board[next_r][next_c])
                                
                                if L <= diff <= R:
                                    visited[next_r][next_c] = 1
                                    q.append((next_r, next_c))
                                    alliance.append((next_r, next_c))
                                    sum_population += board[next_r][next_c]
                
                # 연합이 형성되었다면 (나 자신 제외 2개 이상)
                if len(alliance) > 1:
                    is_moved = True
                    avg_pop = sum_population // len(alliance)
                    
                    # 값 업데이트
                    for r, c in alliance:
                        board[r][c] = avg_pop
                    
                    # [Debug] 연합이 형성되는 순간 포착
                    if DEBUG_MODE:
                        print(f"  👉 연합 형성! 좌표: {alliance}, 평균값: {avg_pop}")

    if is_moved:
        total_days += 1
    else:
        break # 더 이상 이동 없으면 즉시 종료

print(total_days)