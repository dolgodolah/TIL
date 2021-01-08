import sys
input = sys.stdin.readline

dx = [0,-1,1,0,0]
dy = [0,0,0,1,-1]
R,C,M = map(int,input().split())
graph=[[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z=map(int,input().split())
    graph[r-1][c-1]=[s,d,z] #속력, 이동방향, 크기

def fish(idx):
    global score
    for i in range(R):
        if graph[i][idx]:
            score+=graph[i][idx][2]
            graph[i][idx]=[]
            break
def move_shark():
    temp_graph = [[[] for _ in range(C)] for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if graph[i][j]:
                x,y=i,j
                speed, direction, size = graph[x][y][0],graph[x][y][1],graph[x][y][2]
                while speed>0:
                    x,y = x+dx[direction],y+dy[direction]
                    if 0<=x<R and 0<=y<C:
                        speed-=1
                    else:
                        x,y=x-dx[direction],y-dy[direction]
                        if direction==1:
                            direction=2
                        elif direction==2:
                            direction=1
                        elif direction==4:
                            direction=3
                        elif direction==3:
                            direction=4
                if temp_graph[x][y]:
                    if temp_graph[x][y][2]<size:
                        temp_graph[x][y]=[graph[i][j][0],direction,size]
                else:
                    temp_graph[x][y]=[graph[i][j][0],direction,size]
    return temp_graph

score = 0
for idx in range(C):
    fish(idx)
    # for i in graph:
    #     print(i)
    # print()
    graph = move_shark()
    # for p in graph:
    #     print(p)
    # print()
    # print()
print(score)
