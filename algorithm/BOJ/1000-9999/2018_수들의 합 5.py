n=int(input())
count=n
answer=0
while count>0:
    tmp = 0
    for i in range(count,0,-1):
        tmp+=i
        if tmp>=n:
            break
    if tmp==n:
        answer+=1
    count-=1
print(answer)