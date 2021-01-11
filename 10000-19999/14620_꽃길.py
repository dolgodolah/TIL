import sys
from itertools import permutations
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dx = [-1,1,0,0]
dy = [0,0,-1,1]
visited = [[False]*n for _ in range(n)]
answer = int(10e9)
def dfs(seed,cost):
    global answer
    if cost>=answer: #같을 때도 return해줌으로서 시간 단축하자.
        return
    if seed == 3:
        # print(cost)
        # for i in visited:
        #     print(i)
        # print()
        answer = cost
        return
    for i in range(n):
        for j in range(n):
            # 해당 좌표(i,j)에 꽃을 심을 수 있는지 판단한다.
            # 화단 밖으로 꽃잎이 나가게 된다면 그 꽃은 죽어버리고 만다.
            if not 0<=i+1<n or not 0<=i-1<n or not 0<=j+1<n or not 0<=j-1<n:
                continue
            # 다른 꽃잎(혹은 꽃술)과 닿게 될 경우 두 꽃 모두 죽어버린다.
            if visited[i+1][j]==True or visited[i-1][j]==True or visited[i][j+1]==True or visited[i][j-1]==True:
                continue

            #꽃을 심을 수 있다고 판단되면 (i,j)중심과 상하좌우 네방향에 꽃을 심는다.(방문처리)
            for k in range(4):
                visited[i+dx[k]][j+dy[k]]=True
                cost+=graph[i+dx[k]][j+dy[k]]
            visited[i][j]=True
            cost+=graph[i][j]
            dfs(seed+1,cost)
            for k in range(4):
                visited[i+dx[k]][j+dy[k]]=False
                cost-=graph[i+dx[k]][j+dy[k]]
            visited[i][j]=False
            cost-=graph[i][j]

dfs(0,0)
print(answer)


            