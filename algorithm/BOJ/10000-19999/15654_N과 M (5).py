from itertools import permutations
n,m=map(int,input().split())
ls=list(map(int,input().split()))
ls.sort()

for i in permutations(ls,m):
    print(*i)