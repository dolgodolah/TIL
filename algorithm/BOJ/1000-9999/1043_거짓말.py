import sys
from collections import deque
input=sys.stdin.readline
N,M=map(int,input().split())
people=list(map(int,input().split())) # 처음 진실을 알고있는 사람들


graph=[[] for _ in range(N+1)] # 처음 진실을 알고있는 사람들과 같은 파티에 있는 사람들을 알기위한 리스트
parties=[] # 각 파티마다 참여하는 사람들을 담을 리스트
for _ in range(M):
    participant=list(map(int,input().split()))
    parties.append(participant)
    if participant[0]==1:
        continue
    for i in range(2,len(participant)): # 같은 파티 참여자들끼리 그래프를 연결해준다.
        graph[participant[1]].append(participant[i])
        graph[participant[i]].append(participant[1])
# print(graph)

def bfs(x):
    global ls
    queue=deque()
    queue.append(x)
    visited=[False]*(N+1)
    visited[x]=True
    while queue:
        x=queue.popleft()
        ls[x]=1
        for i in graph[x]:
            if visited[i]==False:
                visited[i]=True
                queue.append(i)

ls=[0 for _ in range(N+1)] #최종적으로 진실을 알고있는(알게된) 사람들 리스트
for i in range(1,len(people)): # 처음 진실을 알고있는 사람들과 같은 파티에 있는지 bfs를 통해 확인한다.
    bfs(people[i])

answer=0
for party in parties:
    for i in party[1:]:
        if ls[i]==1: #참가자 중 한명이라도 진실을 할면 탐색을 멈춘다.
            break
    else: #파티 참가자 모두 진실을 모를 때
        answer+=1
print(answer)