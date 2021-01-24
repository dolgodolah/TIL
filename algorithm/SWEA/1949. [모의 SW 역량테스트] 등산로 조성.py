# 문제 설명이 부족하다는 댓글을 보기 잘했다.
# 쉽게 구현하고 제출했는데 49개에서 오답이 나왔고 댓글을 읽어보던 중
# "봉우리 선택을 먼저 고정하고, 그 이후에 깎는다는 구절이 들어가야 될 것 같네요." 라는 댓글을 보고
# 어디가 틀렸는지 바로 느낌이 왔다. 봉우리를 깎고 가장 높은 봉우리를 구하는 것이 아닌
# 가장 높은 봉우리를 구해놓고 봉우리를 깎는 방식이었다.
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]
def get_max():
    max_v=0
    ls = []
    #가장 높은 봉우리의 높이를 구한다.
    for i in range(n):
        for j in range(n):
            if graph[i][j]>max_v:
                max_v=graph[i][j]

    for i in range(n):
        for j in range(n):
            if graph[i][j]==max_v:
                ls.append((i,j))
    return ls

def get_road(ls):
    temp_answer = 0
    for x,y in ls: #가장 높은 봉우리들마다 최대 등산로 길이가 몇인지 구한다.
        queue = deque()
        queue.append((x,y,1))
        while queue:
            x,y,cnt=queue.popleft()
            temp_answer=max(temp_answer,cnt)
            for i in range(4):
                if 0<=x+dx[i]<n and 0<=y+dy[i]<n:
                    nx,ny=x+dx[i],y+dy[i]
                    if graph[nx][ny]<graph[x][y]:
                        queue.append((nx,ny,cnt+1))
    return temp_answer

T = int(input())
for t in range(1,T+1):
    n,k=map(int,input().split()) #지도의 한 변의 길이 N, 최대 공사 가능 깊이 K
    graph=[]
    for _ in range(n):
        graph.append(list(map(int,input().split())))
    

    ls = get_max()
    answer = 0
    #(x,y)마다 k만큼 깍을 때 가장 긴 등산로 길이가 몇인지 구한다.
    for x in range(n):
        for y in range(n):
            for i in range(k+1):
                if not graph[x][y]-i>=0:
                    break
                graph[x][y]-=i
                answer = max(answer,get_road(ls))
                graph[x][y]+=i
    print(f"#{t} {answer}")