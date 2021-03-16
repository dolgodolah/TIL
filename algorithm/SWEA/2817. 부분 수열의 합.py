from itertools import combinations
T=int(input())
for t in range(1,T+1):
    n,k=map(int,input().split())
    ls=list(map(int,input().split()))
    answer=0
    for i in range(1,len(ls)+1):
        for j in combinations(ls,i):
            if sum(j)==k:
                answer+=1
    print(f"#{t} {answer}")