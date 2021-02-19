import sys
from collections import deque
input = sys.stdin.readline
n,m=map(int,input().split())
select=list(map(int,input().split()))
select=deque(select)
queue=[i for i in range(1,n+1)]
queue=deque(queue)
answer=0
while select:
    # print(queue)
    if select[0]==queue[0]:
        select.popleft()
        queue.popleft()
    else:
        answer+=1
        if queue.index(select[0]) <= len(queue)//2:
            queue.append(queue.popleft())
        else:
            queue.appendleft(queue.pop())
print(answer)
