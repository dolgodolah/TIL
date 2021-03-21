T=int(input())


for t in range(1,T+1):
    p,q=map(int,input().split())
   
    #&에 대한 연산
    def calc(value):
        tmp=0 
        cnt=0 #해당 p,q가 몇번째 줄에 있는지
        while tmp<value:
            cnt+=1
            tmp+=cnt
        a=cnt
        b=1

        for i in range(cnt):
            if tmp-i==value:
                break
            a-=1
            b+=1
        return a,b
    def calc2(x,y):
        tmp=0
        cnt=0
        while cnt<x:
            cnt+=1
            tmp+=cnt
        for _ in range(y-1):
            tmp+=cnt
            cnt+=1
        return tmp

    a=calc(p)
    b=calc(q)
    x=a[0]+b[0]
    y=a[1]+b[1]
    print(f"#{t} {calc2(x,y)}")
