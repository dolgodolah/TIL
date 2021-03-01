#시,분,초에 올수있는 숫자들의 조건에 맞춰 백트래킹을 구현했다.

time=input().split(":")

answer=0
visited=[False]*3
def dfs(idx,visited):
    global answer
    if idx==3:
        answer+=1
        return
    for i in range(len(time)):
        if visited[i]==False:
            if idx==0 and 1<=int(time[i])<=12:
                visited[i]=True
                dfs(idx+1,visited)
                visited[i]=False
            elif idx==1 and 0<=int(time[i])<=59:
                visited[i]=True
                dfs(idx+1,visited)
                visited[i]=False
            elif idx==2 and 0<=int(time[i])<=59:
                visited[i]=True
                dfs(idx+1,visited)
                visited[i]=False
dfs(0,visited)
print(answer)
