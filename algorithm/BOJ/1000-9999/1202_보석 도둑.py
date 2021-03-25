# 첫번째 시도(시간초과) : 그리디 알고리즘으로만 생각해서 풀었다.
# 두번째 시도(1116ms) : 그리디 알고리즘 + 우선순위큐(힙큐)를 이용해서 풀었다.

# 기본적으로 그리디 탐색을 해야한다. 가방별로 가성비 좋은 보석을 넣기 위해서는
# 수용할 수 있는 무게가 적은 가방부터 수용할 수 있는 보석 중 가성비 좋은 보석을 넣는 것이다.(가방 수용무게를 오름차순으로 탐색하자는 말)

# 그리디 알고리즘을 구현하기 위해서는 이중포문으로 n^2의 시간복잡도를 가지는데 데이터 범위가 크다.
# 이를 해결하기 위해서 우선순위큐(힙)을 이용했다.
# 예를 들어 10kg을 수용할 수 있는 가방을 탐색하고 있다면 이 가방이 수용할 수 있는 모든 보석들을 v를 기준으로 최대힙에 push한다.
# push 과정이 끝나고 최대힙에서 하나를 pop하면 해당 가방(10kg)이 가장 가성비 좋은 보석을 넣을 수 있게 된다.
# 그 다음 20kg을 수용할 수 있는 가방을 탐색한다고 해보자. 10kg 때 구성된 heapq에 이어서 20kg까지의 보석도 최대힙에 push한다.
# push 과정이 끝나면 하나를 pop하여 해당 가방(20kg)에서 가장 가성비 좋은 보석을 넣을 수 있게 된다.
from heapq import heappop, heappush
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
gem=[]
for _ in range(n):
    m,v=map(int,input().split())
    heappush(gem,(m,v)) #무게를 기준으로 최소힙에 push

bag=[]
for _ in range(k):
    bag.append(int(input()))
bag.sort() #무게가 작은 가방부터 탐색하는 그리디 알고리즘을 위해 무게 기준으로 오름차순 정렬
answer=0
tmp=[] #해당 가방이 수용할 수 있는 보석들을 담을 maxheap
for i in range(k):
    while gem and bag[i]>=gem[0][0]: #bag[i]가 수용할 수 있는 무게의 보석들을 tmp에 push한다.
        m,v=heappop(gem)
        heappush(tmp,-v) #maxheap으로 구성

    if tmp: #위 과정이 끝나면 tmp중에서 가치가 가장 높은 보석을 꺼낸다.
        answer-=heappop(tmp)
print(answer)

