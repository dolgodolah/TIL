# 중복되는 수열을 여러 번 출력하지 않으려면 수를 입력받을 때 중복을 제거하면 된다. set을 통해 중복을 제거하고 다시 list형으로 바꿔줬다.
n,m=map(int,input().split())
ls=list(set(map(int,input().split())))
ls.sort()
answer=[]
def dfs(cnt,nums,start):
    global answer
    if cnt==m:
        print(*nums)
        return
    
    for i in range(start,len(ls)):
        nums.append(ls[i])
        dfs(cnt+1,nums,i)
        nums.pop()
dfs(0,[],0)