# 문제에서 주어진 데이터들이 많아 이해하는데 시간이 걸렸다.
# 상금에 대한 정보들을 입력받고 상금을 내림차순으로 정렬한다.
# 즉 가장 높은 상금부터 스티커를 소모시키고, 이미 0개인 경우에는 다음 상금(그 다음 큰 금액)으로 넘어간다.

import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n,m=map(int,input().split())
    money=list()
    for _ in range(n):
        info=list(map(int,input().split()))
        money.append((info[1::])) #주어진 info에서 필요한 스티커 개수와 상금에 대해서만 money에 append한다.
    sticker=list(map(int,input().split()))
    money.sort(key=lambda x:x[-1],reverse=True) # 그리디 알고리즘을 위해 상금 기준 내림차순으로 정렬
    i=0
    answer=0
    while i<n:
        for j in range(len(money[i])-1):
            if sticker[money[i][j]-1]==0: #해당 상금을 받기 위한 스티커가 부족할 경우
                i+=1 #다음 상금을 탐색한다.
                break
        else: #해당 상금을 받을 수 있을 경우(스티커가 모두 충분할 경우)
            answer+=money[i][-1] #해당 상금을 더하고
            for j in range(len(money[i])-1):
                sticker[money[i][j]-1]-=1 #해당 상금에 필요한 스티커들 개수를 하나씩 줄인다.
    print(answer)
            