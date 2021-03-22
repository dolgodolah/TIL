T=int(input())

for t in range(1,T+1):
    money=[50000,10000,5000,1000,500,100,50,10]
    answer=[0,0,0,0,0,0,0,0]
    n=int(input())
    for i in range(8):
        answer[i]=n//money[i]
        n-=money[i]*answer[i]
    print(f"#{t}")
    print(*answer) 