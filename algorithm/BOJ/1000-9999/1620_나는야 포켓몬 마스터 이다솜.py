# input=sys.stdin.readline 으로 시간을 줄이자.
# 문자열 입력의 경우 '\n' 제거를 위해 .strip()을 해주자.

import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic1=dict()
dic2=dict()
for i in range(1,n+1):
    name=input().strip()
    dic1[name]=str(i)
    dic2[str(i)]=name

# print(dic1)
# print(dic2)
for _ in range(m):
    query=input().strip()
    if query.isnumeric():
        print(dic2[query])
    else:
        print(dic1[query])