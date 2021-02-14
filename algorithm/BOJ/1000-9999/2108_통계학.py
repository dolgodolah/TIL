n=int(input())
ls=[]
for _ in range(n):
    ls.append(int(input()))
print(round(sum(ls)/n))
print(sorted(ls)[n//2])
dic = dict()
for i in ls:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
tmp = sorted(dic.items(),key=lambda x:(-x[1],x[0]))
num1=tmp.pop(0)
if tmp:
    num2=tmp.pop(0)
    if num1[1]==num2[1]:
        print(num2[0])
    else:
        print(num1[0])
else:
    print(num1[0])
print(max(ls)-min(ls))
