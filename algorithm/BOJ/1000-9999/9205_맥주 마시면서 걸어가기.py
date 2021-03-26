# bfs로 간단히 구현할 수 있었는데 bfs 문제를 알아채는데 너무 오래걸렸다.
# 넓이우선탐색이기때문에 해당 좌표에서 갈수있는 가장 가까운 좌표들을 탐색한다.

import sys
from collections import deque
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    n=int(input())
    ls=list()
    start_x,start_y=map(int,input().split())
    store=list()
    for _ in range(n):
        x,y=map(int,input().split())
        store.append((x,y))
    end_x,end_y=map(int,input().split())
    store.append((end_x,end_y))
    answer=False
    def bfs():
        global answer
        queue=deque()
        queue.append((start_x,start_y))
        visited=[False]*(n+1)
        while queue:
            x,y=queue.popleft()
            if x==end_x and y==end_y:
                answer=True
                return
            for i in range(len(store)):
                if visited[i]==False:
                    if abs(store[i][0]-x)+abs(store[i][1]-y)<=1000: #거리가 1000을 넘으면 맥주가 20개보다 더 필요하기때문에 갈수없다.
                        visited[i]=True
                        queue.append((store[i][0],store[i][1]))
    bfs()
    if answer:
        print("happy")
    else:
        print("sad")