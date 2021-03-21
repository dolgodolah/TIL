from itertools import permutations

T=int(input())
for t in range(1,T+1):
    n=int(input())
    ls=list(map(int,input().split()))
    answer=0
    for i in range(1,n+1):
        for j in permutations(ls,i):
            left=set(j)
            right=set(ls)-left
            left+=(0,)*(n-len(left))
            print(left)
    print(answer)
