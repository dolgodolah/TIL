#itertools 라이브러리의 combinations를 이용한 풀이와
#백트래킹으로 직접 구현한 풀이다.

import sys
from itertools import combinations

n,s=map(int,input().split())
ls=list(map(int,input().split()))
result=0
for i in range(1,n+1):
    for j in combinations(ls,i):
        if sum(j)==s:
            result+=1
print(result)


# import sys
# from itertools import combinations

# n,s=map(int,input().split())
# ls=list(map(int,input().split()))
# result=0
# temp=[]
# def check(ls):
#     if sum(ls)==s:
#         return True
#     return False

# def dfs(cnt,idx):
#     global answer
#     if cnt==n:
#         return
#     for i in range(idx,n):
#         temp.append(ls[i])
#         if check(temp):answer+=1
#         dfs(cnt+1,i+1)
#         temp.pop()
# answer = 0
# dfs(0,0)
# print(answer)
        