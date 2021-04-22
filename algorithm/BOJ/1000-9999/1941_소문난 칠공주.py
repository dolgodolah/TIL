# combinations를 이용해 7명 학생의 조합을 모두 탐색한다.
# 해당 조합에 대해서 bfs 탐색을 통해 7명이 모두 인접하는지 확인한다.
# 7명이 모두 인접하고, S>Y일 때 answer+=1 해준다.

from itertools import combinations
from collections import deque

board=list()
for _ in range(5):
    board.append(list(input()))
dx=[-1,1,0,0]
dy=[0,0,-1,1]

ls=list()
for i in range(5):
    for j in range(5):
        ls.append((i,j))
answer=0 
def check(students):
    global answer
    queue=deque()
    queue.append(students[0])
    visited=[[False]*5 for _ in range(5)]
    visited[students[0][0]][students[0][1]]=True
    cnt=1
    S,Y=0,0
    while queue:
        x,y=queue.popleft()
        if board[x][y]=='S':S+=1
        else:Y+=1
        for i in range(4):
            nx,ny=x+dx[i],y+dy[i]
            if (nx,ny) in students:
                if visited[nx][ny]==False:
                    visited[nx][ny]=True
                    queue.append((nx,ny))
                    cnt+=1
    if cnt==7 and S>Y:
        answer+=1

for i in combinations(ls,7):
    check(i)
print(answer)