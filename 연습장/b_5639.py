import sys
from collections import defaultdict 
inputs = sys.stdin.readlines 

tree = defaultdict(list)

nodes = list(map(int, inputs()))
print(inputs)
print(nodes)

# def insert(cur, v):
    # tree