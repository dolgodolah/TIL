from collections import deque

T = int(input())
for t in range(1,T+1):
    answer = 0
    e,n=map(int,input().split())
    ls = list(map(int,input().split()))
    root = [[] for _ in range(e+2)]
    for i in range(0,len(ls)-1,2):
        root[ls[i]].append(ls[i+1])
    def bfs(x):
        global answer
        queue = deque()
        queue.append(x)
        answer+=1
        while queue:
            node = queue.popleft()
            for i in root[node]:
                queue.append(i)
                answer+=1
    bfs(n)
    print(f"#{t} {answer}")