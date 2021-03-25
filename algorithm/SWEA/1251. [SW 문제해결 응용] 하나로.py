# 최소스패닝트리(MST)
# 데이터의 입력이 두 정점을 연결한 간선에 대한 정보가 아닌 좌표값으로 주어져서
# 간선에 대한 비용 정보로 어떻게 바꿔야하는지 몰랐다. 
T=int(input())
for t in range(1,T+1):
    n=int(input())
    x=list(map(int,input().split()))
    y=list(map(int,input().split()))
    E=float(input())
    cost=[]

    for i in range(n):
        for j in range(i+1,n):
            tmp=E*(abs((x[i]-x[j])**2+(y[i]-y[j])**2))
            cost.append((i,j,tmp))
    cost.sort(key=lambda x:x[2])
    root=[i for i in range(n)]

    def find(v):
        if v!=root[v]:
            root[v]=find(root[v])
            return root[v]
        else:
            return v
    answer=0
    for c in cost:
        a,b=c[0],c[1]
        if find(a)!=find(b):
            root[find(a)]=find(b)
            answer+=c[2]
    print(f"#{t} {round(answer)}")
