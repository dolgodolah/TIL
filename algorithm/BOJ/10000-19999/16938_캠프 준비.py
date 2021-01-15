# 주어진 문제 난이도들의 모든 조합에서 아래 조건을 만족하는지 판단한다.
# L보다 크거나 같고, R보다 작거나 같아야 하고 가장 어려운 문제와 가장 쉬운 문제의 난이도 차이는 X보다 크거나 같아야 한다


import sys
from itertools import combinations
input = sys.stdin.readline
def check(ls):
    if not l<=sum(ls)<=r:
        return False
    if not max(ls)-min(ls)>=x:
        return False
    
    return True


n,l,r,x=map(int,input().split())
ls = list(map(int,input().split()))
answer = 0
for i in range(1,n+1): # 출제할 문제 수
    for j in combinations(ls,i): # i개의 문제를 낼 때 나올 수 있는 조합
        if check(j):
            answer+=1
print(answer)