T=int(input())
for t in range(1,T+1):
    month=[0,31,28,31,30,31,30,31,31,30,31,30,31]
    a,b,c,d=map(int,input().split())
    answer=sum(month[:c])+d-(sum(month[:a])+b)+1
    print(f"#{t} {answer}")