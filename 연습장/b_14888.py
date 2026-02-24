import sys
input = sys.stdin.readline



def do_exp(a,b,exp):
    if exp == "+":
        return a+b 
    if exp == "-":
        return a-b 
    if exp == "*":
        return a*b 
    if exp == "//":
        if a< 0 and b > 0:
            return -(abs(a) // b)
        return a//b    
                        

def dfs(depth, path):
    global ans_max
    global ans_min
    if depth == len(exps):
        save_num = nums[0]
        for i in range(1,len(nums)):
            save_num = do_exp(save_num,nums[i],exps[path[i-1]])
        ans_max = max(ans_max,save_num)
        ans_min = min(ans_min,save_num)
        # print(path)
        return 
    for i in range(len(exps)):    
        if i not in path:
            next_path = path + [i]
            dfs(depth + 1, next_path)
            
N = int(input())
nums = list(map(int, input().split()))
ex_nums = list(map(int, input().split()))

exps = []
for i in range(4):
    for j in range(ex_nums[i]):
        if i == 0:
            exps.append("+")
        if i == 1:
            exps.append("-")
        if i == 2:
            exps.append("*")
        if i == 3:
            exps.append("//")

# print(exps)
ans_max = -sys.maxsize
ans_min = sys.maxsize
dfs(0, [])
print(ans_max)
print(ans_min)
