import copy
from itertools import combinations
n,m,d=map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))
graph.append([0]*m)#궁수가 위치할 성 위치 추가

def get_score(graph):
    temp_graph = copy.deepcopy(graph)
    died = [[False]*m for _ in range(n)]
    score = 0
    while True:

        # 공격
        for i in range(m):
            if temp_graph[n][i]==1:#궁수 위치 찾으면
                shoot = 0 #궁수 사격 여부
                for j in range(1,d+1):#거리순으로

                    #왼쪽부터(j==1일때는 수행x)
                    for k in range((j*2-1)//2):
                        if -1<i-j+1+k<m and -1<n-1-k<n and temp_graph[n-1-k][i-j+1+k]==1:
                            if died[n-1-k][i-j+1+k]==False:
                                died[n-1-k][i-j+1+k]=True
                            shoot = 1
                            break
                    if shoot>0:
                        break
                    
                    #가운데
                    if -1<n-j<n and temp_graph[n-j][i]==1:
                        if died[n-j][i]==False:
                            died[n-j][i]=True
                        break
                    
                    #오른쪽
                    for k in range((j*2-1)//2):
                        if -1<n-j+k+1<n and -1<i+k+1<m and temp_graph[n-j+k+1][i+k+1]==1:
                            if died[n-j+k+1][i+k+1]==False:
                                died[n-j+k+1][i+k+1]=True
                            shoot=1
                            break
                    if shoot>0:
                        break
      
        #궁수 사격 턴 끝나고    
        #해당 턴 점수 계산
        for i in range(n):
            for j in range(m):
                if died[i][j]==True:
                    temp_graph[i][j]=0
                    died[i][j]=False
                    score+=1

        # print("공격 후 모습")
        # for i in temp_graph:
        #     print(i)

        #적 이동
        for i in range(n-1,0,-1):
            for j in range(m):
                temp_graph[i][j]=temp_graph[i-1][j]
        temp_graph[0]=[0]*m

        # print("이동 후 모습")
        # for i in temp_graph:
        #     print(i)
        # print()

        #게임 끝 판별
        temp =0
        for i in range(0,n):
            if sum(temp_graph[i])!=0:
                temp=1
                break
        if temp==0:
            break

    return score
answer = 0

for i in combinations(range(m),3):
    graph[n]=[0]*m
    graph[n][i[0]],graph[n][i[1]],graph[n][i[2]]=1,1,1
    answer = max(get_score(graph),answer)

print(answer)
