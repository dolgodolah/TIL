import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
x,y,direction = map(int,input().split())
graph = []
move_type = [(-1,0),(0,1),(1,0),(0,-1)]
for _ in range(n):
    graph.append(list(map(int,input().split())))

def clean(x,y,direction):
    queue = deque()
    queue.append((x,y,direction))
    graph[x][y] = 2
    cnt = 0
    while queue:
        x,y,direction = queue.popleft()
        # print(x,y,direction,cnt)
        # for i in graph:
        #     print(i)
        # print()
        if direction==0:
            if graph[x][y-1]==0:
                cnt=0
                direction=3
                graph[x][y-1]=2
                queue.append((x,y-1,direction))
            elif cnt==4:
                if graph[x+1][y]==1:
                    break
                else:
                    cnt=0
                    queue.append((x+1,y,direction))
            else:
                direction=3
                queue.append((x,y,direction))
                cnt+=1
        elif direction==1:
            if graph[x-1][y]==0:
                cnt=0
                direction=0
                graph[x-1][y]=2
                queue.append((x-1,y,direction))
            elif cnt==4:
                if graph[x][y-1]==1:
                    break
                else:
                    cnt=0
                    queue.append((x,y-1,direction))
            else:
                direction=0
                queue.append((x,y,direction))
                cnt+=1
        elif direction==2:
            if graph[x][y+1]==0:
                cnt=0
                direction=1
                graph[x][y+1]=2
                queue.append((x,y+1,direction))
            elif cnt==4:
                if graph[x-1][y]==1:
                    break
                else:
                    cnt=0
                    queue.append((x-1,y,direction))
            else:
                direction=1
                queue.append((x,y,direction))
                cnt+=1
        elif direction==3:
            if graph[x+1][y]==0:
                cnt=0
                direction=2
                graph[x+1][y]=2
                queue.append((x+1,y,direction))
            elif cnt==4:
                if graph[x][y+1]==1:
                    break
                else:
                    cnt=0
                    queue.append((x,y+1,direction))
            else:
                direction=2
                queue.append((x,y,direction))
                cnt+=1

clean(x,y,direction)
answer = 0
for i in graph:
    answer += i.count(2)
print(answer)