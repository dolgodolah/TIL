# 다른 사람들 풀이는 평균 200ms대인데 내 풀이는 1800ms가 걸린다.
# 내 풀이는 일단 백트래킹으로 풀었는데, 맛없는 아이스크림의 조합에 대해서만 받아놓고
# 모든 조합에 대해 맛없는 아이스크림의 조합에 속해있는지 확인한다.

# 하지만 좋고 깔끔한 코드는 아이스크림이 최대 200개이므로 모든 아이스크림 조합에 대해 미리 받아놓고
# 모든 조합에 대해 맛없는 조합인지 확인하면 끝이다.

import sys
from collections import deque
input = sys.stdin.readline

n,m=map(int,input().split())

#아이스크림별로 맛없는 조합에 대해서 저장한다.
comb = [[] for _ in range(n+1)] 
for _ in range(m):
    a,b=map(int,input().split())
    comb[a].append(b)
    comb[b].append(a)

result = 0
tasteless = [] # 이 리스트에 있는 아이스크림은 맛없다.
def dfs(cnt,idx):
    global result
    if cnt==3:
        # print(tasteless)
        result +=1
        return
    for i in range(idx,n+1):
        if not i in tasteless: #i번째 아이스크림이 맛없을 아이스크림이 아니면
            for j in comb[i]: #i번째 아이스크림을 추가했을 때 맛없을 아이스크림에 대해서 갱신하고
                tasteless.append(j)
            dfs(cnt+1,i+1) #i번째 아이스크림을 추가한다.
            for j in comb[i]: 
                tasteless.remove(j)

dfs(0,1)
print(result)


# import sys
# input = sys.stdin.readline
# n,m=map(int,input().split())

# #아이스크림이 최대 200종류이므로 미리 모든 아이스크림에 대한 조합을 만든다.
# graph = [[False]*(n+1) for _ in range(n+1)] 

# #맛없는 아이스크림 조합은 True로 갱신한다.
# for i in range(m):
#     a,b=map(int,input().split())
#     graph[a][b]=True
#     graph[b][a]=True
# result = 0
# for i in range(1,n-1):
#     for j in range(i+1,n):
#         for k in range(j+1,n+1):
#             # i번째, j번째, k번째 아이스크림을 골랐을 때 3개 아이스크림의 조합이 서로 다 맞는지 확인한다.
#             if graph[i][j]==False and graph[i][k]==False and graph[j][k]==False:
#                 result+=1
# print(result)