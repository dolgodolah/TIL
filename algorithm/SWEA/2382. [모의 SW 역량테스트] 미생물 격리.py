# 몇 개 까다로운 조건만 구현해주면 되는 문제이다. (시간 싸움)
# 백준에서 청소년 상어 아직 못풀고 넘겼는데 다운그레이드 문제인 느낌이다.
# 실제 맵의 상태를 나타내는 graph 배열과
# graph에서 미생물들의 좌표값이 어딘지 나타내는 virus 배열을 이용했다.

# 청소년상어때도 그렇고 이런 문제는 인덱스 오류 해결하기가 어려워서 끙끙 앓고있는 시간이 많다.
# 이 문제에서는 [x,y]에 있는 미생물이 0이 되어 사라질 때 graph[x][y]가 []가 되게끔 해주고
# virsu 리스트에서 [x,y]의 값을 갖고 있는 인덱스도 []가 되게 해줬다.

# 약품이 있는 구역을 간 미생물에 대한 처리는 virus[i]=[]로 해주면 된다.
# 한 구역에 여러 미생물 군집이 모여 처리를 해줄때는
# virus[virus.index([i,j])]=[] 를 통해 좌표값[i,j]를 가지고 있는 미생물의 인덱스를 알아내어
# 모여 있는 군집 수 - 1만큼 []로 처리해준다.
dx = [0,-1,1,0,0]
dy = [0,0,0,-1,1]
T = int(input())
for t in range(1,T+1):
    n,m,k=map(int,input().split()) #맵크기, 격리시간, 미생물 수
    graph = [[[] for _ in range(n)] for _ in range(n)] #맵의 상태를 나타내는 배열
    virus = [] #미생물들의 위치를 나타내는 배열
    for _ in range(k):
        a,b,c,d=map(int,input().split())
        graph[a][b].append([c,d])
        virus.append([a,b])

    
    # for i in graph:
    #     print(i)
    # print(virus)

    for _ in range(m):

        #미생물들의 이동
        for i in range(len(virus)):
            if not virus[i]:continue #해당 미생물이 []이면, 즉 죽은 미생물이면 넘어간다.
            x,y=virus[i]
            v,d=graph[x][y].pop(0)
            if 0<x+dx[d]<n-1 and 0<y+dy[d]<n-1: #약품없는 구역 이동할때
                nx,ny=x+dx[d],y+dy[d]
                graph[nx][ny].append([v,d])
                virus[i]=[nx,ny]
            elif x+dx[d]==0 or x+dx[d]==n-1 or y+dy[d]==0 or y+dy[d]==n-1:#약품있는 구역 이동할때
                nx,ny=x+dx[d],y+dy[d]
                #미생물 수 반으로 줄어들고, 이동방향 반대로 바뀐다.
                v//=2
                if v==0:
                    virus[i]=[]
                    continue #미생물이 다 죽어 없으면 군집이 사라진다.
                if d==1:graph[nx][ny].append([v,2])
                elif d==2:graph[nx][ny].append([v,1])
                elif d==3:graph[nx][ny].append([v,4])
                elif d==4:graph[nx][ny].append([v,3])
                virus[i]=[nx,ny]

        #합쳐진 군집에 대한 처리
        for i in range(n):
            for j in range(n):
                if len(graph[i][j])>1: #한 좌표에 군집이 둘 이상이면
                    for _ in range(virus.count([i,j])-1): #모여있는 수-1만큼 [] 처리해준다.
                        virus[virus.index([i,j])]=[]
                    max_v = 0
                    final_d = 0
                    sum_v = 0
                    #미생물 수는 합쳐지고 미생물 수가 더 많았던 군집의 이동방향으로 된다.
                    for v,d in graph[i][j]:
                        sum_v+=v
                        if v>max_v:
                            max_v=v 
                            final_d=d
                    graph[i][j]=[[sum_v,final_d]]

        # for i in graph:
        #     print(i)
        # print()
    answer = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j]:
                answer+=graph[i][j][0][0]
    print(f'#{t} {answer}')
                

