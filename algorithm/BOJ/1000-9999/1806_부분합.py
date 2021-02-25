# 예전에 풀고 3444ms로 통과했던 문제인데 최근 투포인터를 공부하고 나서 새로 풀어봤다.
# 카카오 코딩테스트 문제에서 보석사는 문제(?)에서 했던 방식처럼 탐색했다.

# 처음에는 부분합을 구할 때 sum(ls[left:right])를 이용했는데 이는 투포인터를 쓴 이유를 없앤달까?
# 부분합을 저장할 value 변수를 만들어 매번 갱신했다.

n,m=map(int,input().split())
ls=list(map(int,input().split()))

left=0
right=0
value=ls[0]
answer=int(10e9)
while right<n and left<=right:
    if value<m:
        right+=1
        if right==n:
            break
        value+=ls[right]
    else: #value>=m
        answer=min(answer,right-left+1)
        value-=ls[left]
        left+=1
if answer==int(10e9):
    print(0)
else:
    print(answer)