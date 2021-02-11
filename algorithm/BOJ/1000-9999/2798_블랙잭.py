from itertools import combinations

n,m=map(int,input().split())
nums=list(map(int,input().split()))

answer=0
min_v=int(10e9)
for i in combinations(nums,3):
    if sum(i)>m:
        continue
    if sum(i)==m:
        answer=m
        break
    if min_v>m-sum(i):
        min_v=m-sum(i)
        answer=sum(i)
print(answer)