import sys
input = sys.stdin.readline 

#트리를 class로 직접 구현하는건 비용이 너무 많이듬, 이 문제에선 간단히 딕셔너리를 이용해 트리순회를 구현함! 

N = int(input())
tree = {}
for i in range(N):
    me, l, r = input().split()
    tree[me] = [l, r]

# print(tree)

def pre(node):
    if node == '.':
        return
    print(node, end ='')
    pre(tree[node][0])
    pre(tree[node][1])
    
def middle(node):
    if node == '.':
        return
    middle(tree[node][0])
    print(node, end ='')
    middle(tree[node][1])

def post(node):
    if node == '.':
        return
    post(tree[node][0])
    post(tree[node][1])
    print(node, end ='')
    
pre('A')
print("")
middle('A')
print("")
post('A')
