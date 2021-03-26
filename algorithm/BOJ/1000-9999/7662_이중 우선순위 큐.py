# 파이썬의 heapq를 이용해 maxheap과 minheap을 만들고 큐에 존재하는 수들을 카운팅한 dic을 만들어준다.
# num를 추가할 때는 maxheap과 minheap에 맞춰 각각 push해주고 dic[num]+=1 해준다.(최종적으로 dic에 존재하는 num들이 큐에 남아있는 숫자일것이다.)
# num를 제거할 때를 주의해야한다.
# minheap에서 num를 pop하고 dic[num]-=1을 해주어 0이 됐다고 하자. 하지만 maxheap에서는 그대로 있다.
# 다음 연산이 maxheap에서 pop을 한 num는 이미 dic에서 0이기 때문에 존재하지 않는 숫자이다. dic에 존재하는 숫자의 카운팅을 -1할 때까지 maxheap에서 pop해주면 된다.

import sys
from heapq import heappop,heappush
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    maxheap=[]
    minheap=[]
    dic=dict()
    for _ in range(n):
        command=input().split()
        if command[0]=='I':
            #minheap과 maxheap에 맞춰 push해준다.
            heappush(minheap,int(command[1]))
            heappush(maxheap,-int(command[1]))

            #실제 queue에 존재하는 숫자는 dic에 기록한다.
            if int(command[1]) in dic:
                dic[int(command[1])]+=1
            else:
                dic[int(command[1])]=1
        else:
            if command[1]=='-1':
                while minheap: #maxheap에서 제거됐지만 minheap에서는 제거되지 않은 수가 있을 수 있다.
                    num=heappop(minheap) #실제 dic에 존재하는 숫자가 삭제될 때까지 minheap에서 pop해준다.
                    if num in dic and dic[num]>0: 
                        dic[num]-=1
                        if dic[num]==0:
                            del dic[num]
                        break
            else:
                while maxheap:
                    num=-heappop(maxheap)
                    if num in dic and dic[num]>0:
                        dic[num]-=1
                        if dic[num]==0:
                            del dic[num]
                        break

    if dic:
        print(max(dic),min(dic))
    else:
        print("EMPTY")
