# 처음에 bfs로 풀었는데 메모리 초과가 뜬다. 데이터 범위를 보니 1<=A,B<=10^9이다.
# visited = [False]*10^9, 메모리 초과다.
# dfs로 푸니까 쉽게 통과했다. 소스코드 싹 갈아엎기 전에 데이터 범위보고 생각을 해보는 습관을 가져야겠다.

a,b=map(int,input().split())
answer = -2
def dfs(cnt,result):
    global answer
    if result==b:
        answer=cnt
        return
    if result>b:
        return

    dfs(cnt+1,result*2)
    temp = int(str(result)+'1')
    dfs(cnt+1,temp)
dfs(0,a)
print(answer+1)