#n의 최대 크기는 500,000이고 m의 최대 크기도 500,000이므로 이중포문을 돌리면 시간초과가 발생한다.
#딕셔너리를 활용하여 n만큼 주어진 card들을 dic에 갱신하고
#m만큼 또 탐색하여 num이 dic안에 있는지 확인한다.
n=int(input())
cards=list(map(int,input().split()))
m=int(input())
nums=list(map(int,input().split()))

answer=[]
dic=dict()
for card in cards:
    if card in dic:
        dic[card]+=1
    else:
        dic[card]=1

for num in nums:
    if num in dic:
        answer.append(dic[num])
    else:
        answer.append(0)
print(*answer)