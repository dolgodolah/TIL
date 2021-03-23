T=int(input())

def dfs(x,y,diag,diag2):
    global answer
    if x==n:
        answer+=1
        return
    for i in range(n):
        if y[i]==0 and diag[x+i]==0 and diag2[i-x]==0:
            y[i],diag[x+i],diag2[i-x]=1,1,1
            dfs(x+1,y,diag,diag2)
            y[i],diag[x+i],diag2[i-x]=0,0,0


for t in range(1,T+1):
    answer=0
    n=int(input())
    y=[0]*n
    diag=[0]*(2*n-1)
    diag2=[0]*(2*n-1)
    dfs(0,y,diag,diag2)
    print(f"#{t} {answer}")