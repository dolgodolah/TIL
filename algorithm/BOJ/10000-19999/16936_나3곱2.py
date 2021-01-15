import sys


input = sys.stdin.readline

n = int(input())
ls = list(map(int,input().split()))
answer = []
for i in range(n):
    cnt = 0
    temp = ls[i]
    if ls[i]%3==0:
        while True:
            if ls[i]%3!=0:
                break
            ls[i]=ls[i]//3
            cnt+=1
    answer.append((cnt,temp))
answer = sorted(answer,key=lambda x:(-x[0],x[1]))
for i in range(n):
    print(answer[i][1],end=' ')