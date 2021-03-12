#백트래킹으로 구현했다.

from itertools import combinations
N,M=map(int,input().split())

def dfs(cnt,nums,start):
    if cnt==M:
        print(*nums)
        return
    
    for i in range(start,N+1):
        nums.append(i)
        dfs(cnt+1,nums,i)
        nums.pop()

dfs(0,[],1)