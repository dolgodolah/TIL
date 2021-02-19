from collections import deque
n=int(input())
queue=[i for i in range(1,n+1)]
queue=deque(queue)
while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())
print(queue[0])