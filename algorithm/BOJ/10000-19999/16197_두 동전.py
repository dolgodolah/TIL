# 그래프문제라서 bfs와 dfs 두 버전으로 풀어봤다.
# 일단 공통적으로 그래프를 싹 돌아 동전의 위치를 찾아 coin 좌표값을 저장하고
# bfs나 dfs 들어갈 때 그 좌표값을 이용하여 아래 조건을 만족시키는 경우를 찾으면 된다.

#1.동전이 이동하려는 칸이 벽이면, 동전은 이동하지 않는다.
#2.동전이 이동하려는 방향에 칸이 없으면 동전은 보드 바깥으로 떨어진다.
#3.그 외의 경우에는 이동하려는 방향으로 한 칸 이동한다.이동하려는 칸에 동전이 있는 경우에도 한 칸 이동한다.
#4.두 동전 중 하나만 보드에서 떨어뜨리기 위해 버튼을 최소 몇 번 눌러야하는지?

# bfs가 넓이우선이라서 위 조건 중 4번을 만족하는 경우가 찾아지면 그 때가 최소값이 된다.(504ms)
# dfs로 풀면 위 조건을 만족하는 조합을 찾더라도 모든 조합을 다 진행해야 최소값을 알 수 있게 된다. (788ms)
# 이 문제 풀기 전에는 왜 이건 bfs로 풀고 이건 dfs로 풀지? 라는 생각을 했는데 느낌이 왔다.
from collections import deque
n,m=map(int,input().split())

dx = [-1,1,0,0]
dy = [0,0,-1,1]
graph=[]
for _ in range(n):
    graph.append(list(input()))

coin = []
for i in range(n):
    for j in range(m):
        if graph[i][j]=='o':
            coin.append([i,j])
def bfs():
    global answer
    queue = deque()
    queue.append((coin[0][0],coin[0][1],coin[1][0],coin[1][1],1))
    while queue:
        x1,y1,x2,y2,cnt=queue.popleft()
        if cnt>10: #이동횟수가 10번 넘으면 실패로 간주하고 그만!
            answer = -1
            return
        for i in range(4):
            nx1,ny1 = x1+dx[i],y1+dy[i]
            nx2,ny2 = x2+dx[i],y2+dy[i]
            if (not 0<=nx1<n or not 0<=ny1<m) and (not 0<=nx2<n or not 0<=ny2<m): #둘 다 아웃!
                continue
            elif (not 0<=nx1<n or not 0<=ny1<m) and 0<=nx2<n and 0<=ny2<m:#1번만 떨어져
                answer = cnt
                return
            elif 0<=nx1<n and 0<=ny1<m and (not 0<=nx2<n or not 0<=ny2<m):#2번만 떨어져
                answer = cnt
                return
            else: #둘다 안떨어져
                if graph[nx1][ny1]=='#': #이동했는데 벽이라면 좌표 다시 돌려놔
                    nx1,ny1=x1,y1
                if graph[nx2][ny2]=='#': #이동했는데 벽이라면 좌표 다시 돌려놔
                    nx2,ny2=x2,y2
                queue.append((nx1,ny1,nx2,ny2,cnt+1))
answer = -1
bfs()
print(answer)
    


# answer = int(10e9)
# def dfs(x1,y1,x2,y2,direction,cnt):
#     global answer
#     if cnt>10: #버튼 누른 횟수가 10번 넘으면 실패
#         return
#     if cnt>=answer: #갱신된 answer의 값보다 이미 cnt가 커버리면 더 이상 진행할 필요x
#         return

#     nx1 = x1 + dx[direction]
#     ny1 = y1+ dy[direction]
#     nx2 = x2 + dx[direction]
#     ny2 = y2 + dy[direction]

#     #동전이 떨어진다는것은 좌표값이 그래프의 범위를 벗어난거기때문에 벽인지 확인하기 전에 처리한다.
#     #graph[nx1][ny1]=='#'을 하면 안된다는 소리!
#     if (not 0<=nx1<n or not 0<=ny1<m) and (not 0<=nx2<n or not 0<=ny2<m): #1,2번 동전 둘 다 떨어질 때
#         return
#     elif (not 0<=nx1<n or not 0<=ny1<m) and 0<=nx2<n and 0<=ny2<m: #1번 동전만 떨어질 때
#         # print(nx1,ny1)
#         # print(nx2,ny2)
#         # print(cnt)
#         answer = min(answer,cnt)
#     elif 0<=nx1<n and 0<=ny1<m and (not 0<=nx2<n or not 0<=ny2<m): #2번 동전만 떨어질 때
#         # print(nx1,ny1)
#         # print(nx2,ny2)
#         # print(cnt)
#         answer = min(answer,cnt)
    
#     else: #둘다 안떨어졌을 때
#         if graph[nx1][ny1]=='#': #1번 동전을 움직였을 때 벽이면 다시 좌표 되돌린다.
#             nx1,ny1=x1,y1
#         if graph[nx2][ny2]=='#': #2번 동전을 움직였을 때 벽이면 다시 좌표 되돌린다.
#             nx2,ny2=x2,y2
#         for i in range(4):
#             dfs(nx1,ny1,nx2,ny2,i,cnt+1)