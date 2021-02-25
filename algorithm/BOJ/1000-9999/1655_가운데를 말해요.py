# 큐를 두 개 만드는데 하나는 max힙, 다른 하나는 min힙으로 만든다.
# max힙, min힙 순서대로 입력받은 숫자를 push 한다.
# 중간값으로 max힙의 루트값을 출력한다.

# 예를 들어 1,5,2가 입력될 때 max힙=[2,1], min힙=[5]가 된다. 중간값은 2이고 max힙의 루트도 2이다.
# max힙의 루트값보다 min힙의 루트값이 작으면 서로 교체한다.
# 즉 입력받은 수를 정렬하면 max힙[::-1]+min힙[::] 순이 될 것이다.


import sys
from heapq import heappop, heappush
input=sys.stdin.readline
N=int(input())
min_heap=[]
max_heap=[]
for i in range(N):
    x=int(input())
    if len(min_heap)==len(max_heap):
        heappush(max_heap,(-x,x))
    else:
        heappush(min_heap,(x,x))
    
    if min_heap and max_heap[0][1]>min_heap[0][1]:
        min_v=heappop(min_heap)[1]
        max_v=heappop(max_heap)[1]
        heappush(min_heap,(max_v,max_v))
        heappush(max_heap,(-min_v,min_v))
    print(max_heap[0][1])
