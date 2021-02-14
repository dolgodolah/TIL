# 파이썬의 sort는 stable sort이다.(기존의 순서를 유지한다.)

n=int(input())
members=[]
for _ in range(n):
    age,name=input().split()
    members.append((age,name))

members.sort(key=lambda x:int(x[0]))
for member in members:
    print(*member)