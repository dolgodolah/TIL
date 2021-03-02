# 어제 공부했던 밸만포드 알고리즘 문제이다. 
# 이 문제가 가장 기본형인것같다. 저번 문제(1865_웜홀)에서는 출발지점이 따로 없이
# 음의 사이클 존재여부만 판단하면 됐기 때문에 dist[출발지점]=0으로 갱신해줄 필요가 없었지만
# 이번 문제는 출발지점이 1번 노드로 정해져있어 dist[1]=0으로 갱신했고
# 출발지점노드부터 각 노드들마다 if dist[j]!=int(10e9) 조건문을 통해 갱신된 노드인지 확인한다.

# bellmanFord() 수행 후 음의 사이클이 존재하면 -1을 출력하고
# 음의 사이클이 존재하지 않으면 dist테이블을 출력해준다. 갱신된적 없는 노드는 방문하지 못하는 노드이므로 -1을 출력한다.
N,M=map(int,input().split())
graph=[[] for _ in range(N+1)]

for _ in range(M):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def bellmanFord():
    dist=[int(10e9)]*(N+1)
    dist[1]=0
    for i in range(1,N+1):
        for j in range(1,N+1):
            for node,value in graph[j]:
                if dist[j]!=int(10e9) and dist[node]>dist[j]+value:
                    dist[node]=dist[j]+value
                    if i==N:
                        return False
    
    return dist

dist=bellmanFord()
if dist==False:
    print(-1)
else:
    for i in range(2,N+1):
        if dist[i]==int(10e9):
            print(-1)
        else:
            print(dist[i])
