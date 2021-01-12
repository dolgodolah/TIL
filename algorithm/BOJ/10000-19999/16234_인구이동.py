import sys
from collections import deque
input = sys.stdin.readline
n,l,r=map(int,input().split())
graph= []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,0,1,0]
dy = [0,1,0,-1]

def bfs(node):
    q = deque()
    q.append(node)
    population = 0 #인구 수
    num = 0 #연합을 구성한 나라 수
    while q:
        temp = q.popleft()
        for now in queue[temp]:
            if visited[now]==False:
                visited[now]=True
                q.append(now)
                population += graph[now//n][now%n]
                num+=1
    # print(population,num)
    return population//num
def move(node,population):
    val = [False] * (n*n)
    q = deque()
    q.append(node)
    while q:
        temp = q.popleft()
        for now in queue[temp]:
            if val[now]==False:
                val[now]=True
                q.append(now)
                graph[now//n][now%n]=population
answer = 0
while True:
    visited = [False]*(n*n)
    queue = [[] for _ in range(n*n)]
    val = 0
    for x in range(n):
        for y in range(n):
            for i in range(4):
                #해당 나라와 인접위치(상하좌우)에 있는 나라와 인구수를 비교한다.
                if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                    nx,ny=x+dx[i],y+dy[i]
                    #인구수 차이가 L이상 R이하이면 국경을 개방한다.
                    if l<=abs(graph[x][y]-graph[nx][ny])<=r:
                        queue[x*n+y].append(nx*n+ny) # x*n+y번째 도시는 nx*n+ny번째 나라와 국경을 개방한다.

    for node in range(len(queue)):
        if queue[node] and visited[node]==False:
            population = bfs(node) #bfs를 통해 연합을 이루고 있는 각 칸의 인구수(연합의 인구수) / (연합을 이루고 있는 칸의 개수)를 구한다.
            move(node,population) #move를 통해 해당 연합의 인구 이동을 한다.
            
            val+=1
            
    #인구이동이 없다면 종료한다.
    if val==0:
        break
    answer+=1
print(answer)

