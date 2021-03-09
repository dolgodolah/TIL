# dict을 이용해 보도못한 사람을 입력받을 때 이미 dict안에 존재한다면 answer에 추가한다.
n,m=map(int,input().split())
answer=[]
dic=dict()
for _ in range(n):
    dic[input()]=1

for _ in range(m):
    name=input()
    if name in dic:
        answer.append(name)

print(len(answer))
answer.sort()
for i in answer:
    print(i)
