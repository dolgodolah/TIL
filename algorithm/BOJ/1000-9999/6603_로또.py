import sys
from itertools import combinations
input = sys.stdin.readline
while True:
    case = list(map(int,input().split()))
    k=case[0]
    if k==0:
        break
    ls = sorted(case[1:])
    for i in combinations(ls,k):
        for j in combinations(i,6):
            print(*j)
    print()