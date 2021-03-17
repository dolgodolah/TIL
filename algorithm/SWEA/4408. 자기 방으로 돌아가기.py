# room1과 room2는 복도1을 포함하고, room3과 room4는 복도2를 포함하고... room399와 room400은 복도200을 포함한다.
# 즉 복도를 1~200까지 만들어 학생들이 복도를 지나가 겹치는 구간이 어느정도인지 계산하면 된다.

T=int(input())
for t in range(1,T+1):
    n=int(input())
    ls=[0]*201
    for _ in range(n):
        a,b=map(int,input().split())
        if a>b:a,b=b,a #a가 더 크게 주어지는 예외를 처리한다.

        a=(a+1)//2 #1(room)+1 // 2 = 복도1
        b=(b+1)//2 #2(room)+1 // 2 = 복도1
        for i in range(a,b+1):
            ls[i]+=1

    print(f"#{t} {max(ls)}")