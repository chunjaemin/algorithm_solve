import sys
input =sys.stdin.readline 

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

prev_max = [0]*3
cur_max = [0]*3

prev_min = [0]*3
cur_min = [0]*3

for i in range(3):
    prev_max[i] = board[0][i]
    prev_min[i] = board[0][i]
    cur_max[i] = board[0][i]
    cur_min[i] = board[0][i]


# print(prev_max)
# print(cur_max)
# print("")

for i in range(1, N): 
    cur_min[0] = min(prev_min[0], prev_min[1]) + board[i][0]
    cur_min[1] = min(prev_min[0], prev_min[1], prev_min[2]) + board[i][1]
    cur_min[2] = min(prev_min[1], prev_min[2]) + board[i][2]
    
    cur_max[0] = max(prev_max[0], prev_max[1]) + board[i][0]
    cur_max[1] = max(prev_max[0], prev_max[1], prev_max[2]) + board[i][1]
    cur_max[2] = max(prev_max[1], prev_max[2]) + board[i][2]
    
    prev_min[0], prev_min[1], prev_min[2] = cur_min[0], cur_min[1], cur_min[2]
    prev_max[0], prev_max[1], prev_max[2] =  cur_max[0], cur_max[1], cur_max[2]
    
    # print(prev_max)    
    # print(cur_max)
    # print("")

min_ans = min(cur_min[0], cur_min[1], cur_min[2])
max_ans = max(cur_max[0], cur_max[1], cur_max[2])

# for row in prev_min:
#     print(" ".join(map(str, row)))

print(max_ans, min_ans)