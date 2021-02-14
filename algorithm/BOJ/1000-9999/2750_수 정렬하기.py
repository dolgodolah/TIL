n=int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))

ls.sort()
for i in ls:
    print(i)