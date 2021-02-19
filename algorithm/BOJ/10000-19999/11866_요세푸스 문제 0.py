from collections import deque
n,k=map(int,input().split())
queue=[i for i in range(1,n+1)]
queue=deque(queue)
cnt=0
answer=list()
while queue:
    cnt+=1
    tmp=queue.popleft()
    if cnt==k:
        answer.append(tmp)
        cnt=0
        continue
    queue.append(tmp)
print("<",end="")
for i in range(len(answer)-1):
    print(answer[i],end=", ")
print(answer[-1],end=">")