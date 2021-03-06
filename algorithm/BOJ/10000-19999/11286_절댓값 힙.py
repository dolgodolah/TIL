import sys
from heapq import heappush,heappop
input=sys.stdin.readline
N=int(input())
queue=[]
for _ in range(N):
    x=int(input())
    if x==0:
        if queue:
            print(heappop(queue)[1])
        else:
            print(0)
    else:
        heappush(queue,(abs(x),x))
