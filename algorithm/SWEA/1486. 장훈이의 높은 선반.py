# 백트래킹을 활용해 모든 조합들을 탐색해보는데 b보다 크거나 같은 경우들중 작은 값을 answer로 갱신해준다.

T=int(input())
for t in range(1,T+1):
    n,b=map(int,input().split())
    ls=list(map(int,input().split()))
    answer=int(10e9)

    def dfs(result,visited,start):
        global answer
        if result>=b:
            answer=min(result,answer)
            return
        
        for i in range(start+1,len(ls)):
            if visited[i]==False:
                visited[i]=True
                dfs(result+ls[i],visited,i)
                visited[i]=False

    visited=[False]*n
    for i in range(len(ls)):
        visited[i]=True
        dfs(ls[i],visited,i)
        visited[i]=False

    print(f"#{t} {answer-b}")