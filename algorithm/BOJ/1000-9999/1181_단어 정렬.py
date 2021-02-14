n=int(input())
ls=set()
for _ in range(n):
    ls.add(input())

answer = sorted(ls,key=lambda x:(len(x),x))
for i in answer:
    print(i)