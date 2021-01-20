#https://github.com/dolgodolah/TIL/blob/master/algorithm/BOJ/10000-19999/16929_Two%20Dots.py
#dfs로 해당 노드가 사이클을 형성하는지 확인하는 과정이 있어 16929_Two Dots의 풀이법을 활용했다.
#순환선(사이클형성)인지 체크를 하고나서 순환선이 아닌 역(노드)들은 bfs를 통해 순환선까지의 거리를 구한다.
#로직은 맞는거 같은데 자꾸 RecursionError가 발생한다.
#sys.setrecursionlimit(10**5)를 통해서 재귀 최대깊이를 늘릴수 있다고 한다.
#설정 이후에는 다행히 통과되었다.

import sys
from collections import deque
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n=int(input())
graph=[[] for _ in range(n+1)]
for _ in range(n):
    a,b=map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

#사이클 확인하는 dfs
def dfs(node,d):
    global i,result
    if result==True:
        return
    visited[node]=True
    for n in graph[node]:
        if visited[n]==False:
            dfs(n,d+1)
        elif visited[n]==True and n==i and d>1: #1->2->1로 가는 사이클은 취급하지않기 위해서 d가 1보다 클 때만 사이클을 인정한다.
            result=True
            return

#해당 idx역에서 순환선까지 거리가 얼마나 되는지 확인하는 bfs
def bfs(idx):
    queue = deque()
    queue.append((idx,0))
    visited = [False]*(n+1)
    visited[idx]=True
    while queue:
        node,d = queue.popleft()
        if cycle[node]:
            return d
        for i in graph[node]:
            if visited[i]==False:
                visited[i]=True
                queue.append((i,d+1))

cycle = [False]*(n+1)
for i in range(1,n+1):
    visited = [False]*(n+1)
    result=False
    dfs(i,0) #역 별로 순환선인지 확인한다.
    if result:
        cycle[i]=True

for i in range(1,n+1):
    if cycle[i]:
        print(0,end=" ")
    else: #순환선이 아니라면 순환선까지 거리가 얼마나 되는지 bfs로 확인한다.
        print(bfs(i),end=" ")
        