# dfs로 출발지점(1~N)마다 모든 경로를 탐색하여 구해진 비용이 음수인 것을 찾아보았다.(50% 시간초과)
# 벨만포드 알고리즘을 사용해야 한다고 한다.
# 아직 새로운 문제를 풀어보진 않아서 익숙친 않은데 다시 상기시켜보기 위해 적어본다.

# 일단 다익스트라보다 비효율적인 시간복잡도를 가지고 있다. 하지만 음의 가중치를 갖고 있을 때는 벨만포드 알고리즘을 사용한다.
# 음의 가중치를 가지고 있으면 음의 사이클이 발생할 수 있기 때문이다.(무조건 발생하는건 아님)

# 즉, 이 문제는 벨만포드 알고리즘을 통해 해당 노드와 인접한 노드들끼리 음의 사이클이 발생하는지 확인하는 문제이다.
# 문제에서 요구하는 것처럼 여행 후 시간이 되돌아가있으려면 음의 사이클이 존재해야한다.

def bellmanFord():
    global answer
    for i in range(1,N+1):
        for j in range(1,N+1): #해당 j번 노드에서
            for node,value in graph[j]: #인접한 노드들을 검사한다.
                if dist[node]>dist[j]+value:
                    dist[node]=dist[j]+value
                    if i==N: #N번 검사했는데 N번째에도 줄어들면 음의 사이클이 존재한다.
                        answer="YES"
TC=int(input())
for _ in range(TC):
    N,M,W=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        graph[a].append((b,c))
        graph[b].append((a,c))
    for _ in range(W):
        a,b,c=map(int,input().split())
        graph[a].append((b,-c))
    
    answer="NO"
    dist=[int(10e9)]*(N+1)
    bellmanFord()

    print(answer)


# def dfs(x,visited,result,start):
#     global answer
#     if x==start and visited[x]:
#         if result<0:
#             answer="YES"
#     for node,value in graph[x]:
#         if visited[node]==False:
#             visited[node]=True
#             dfs(node,visited,result+value,start)
#             visited[node]=False