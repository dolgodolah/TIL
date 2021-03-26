# 생각을 깊게 해야했던 bfs문제였다. 두 동영상 쌍의 유사도에 대한 정보가 N-1개 주어지는데
# '임의의 두 쌍 사이의 동영상의 유사도를 그 경로의 모든 연결들의 유사도 중 최솟값으로 하기로 했다.'를
# Q개의 query가 주어질때마다 bfs를 통해 탐색하면서 min()을 통해 유사도를 갱신하기로 했다.

import sys
from collections import deque
input=sys.stdin.readline

def bfs(k,v):
    global answer
    queue=deque()
    queue.append((v,int(10e9))) #모든 연결들의 유사도 중 최솟값으로 하기때문에 초기 유사도를 int(10e9)로 한다. 
    visited=[False]*(N+1)
    visited[v]=True
    while queue:
        node,value=queue.popleft()
        for i in graph[node]:
            if visited[i[0]]==False:
                # 임의의 두 쌍 사이의 동영상의 유사도를 그 경로의 모든 연결들의 유사도 중 최솟값으로 하기로 한다.
                # node번 영상까지의 유사도가 value인데 node번 영상과 연결된 i[0]번 영상들의 유사도 i[1] 중 최소값 min(value,i[1])이 v번 영상과 i[0]영상의 유사도가 된다.
                usado=min(value,i[1]) 
                if usado>=k:
                    answer+=1
                visited[i[0]]=True
                queue.append((i[0],usado))

N,Q=map(int,input().split())
graph=[[] for _ in range(N+1)]
for _ in range(N-1):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
for _ in range(Q):
    #쿼리가 주어질 때마다 해당 쿼리에 대한 bfs 탐색을 한다.
    k,v=map(int,input().split())
    answer=0
    bfs(k,v) #v정점으로부터 bfs탐색을 시작해서 유사도가 k이상인 것들을 찾는다.
    print(answer)