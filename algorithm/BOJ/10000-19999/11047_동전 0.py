# 가치가 큰 동전을 최대한 많이 사용해야 가장 적은 동전을 사용할 수 있다.
n,k=map(int,input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
answer=0
coin.sort(reverse=True)
for i in coin:
    if k//i>0:
        answer+=k//i
        k-=k//i*i
    if k==0:
        break
print(answer)