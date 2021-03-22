def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)
def dfs(left,right,cnt,remainder):
    global answer
    if cnt==n:
        answer+=1
        return
    if left>right+remainder:
        answer+=factorial(n-cnt)*(2**(n-cnt))
        return
    for i in range(n):
        if visited[i]==False:
            visited[i]=True
            dfs(left+ls[i],right,cnt+1,remainder-ls[i])
            if left>=right+ls[i]:
                dfs(left,right+ls[i],cnt+1,remainder-ls[i])
            visited[i]=False

T=int(input())
for t in range(1,T+1):
    n=int(input())
    ls=list(map(int,input().split()))
    answer=0
    visited=[False]*n
    dfs(0,0,0,sum(ls))
    print(f"#{t} {answer}")