# 인쇄하고자 하는 문서가 몇번째에 뽑히는지 알아내는 문제이기 때문에
# 다른 문서가 뽑힐 때만 result+=1 해주면 되는데, 자꾸 문서가 뒤로 갈 때도 result+=1을 해줘서 헤맸다.

from collections import deque

t=int(input())
for _ in range(t):
    n,m=map(int,input().split())
    tmp=list(map(int,input().split()))
    queue=list()
    
    for idx,value in enumerate(tmp):
        queue.append((idx,value)) 
    queue=deque(queue)
    result=1
    while queue:
        idx,value=queue[0][0],queue[0][1]
        if value==max(queue,key=lambda x:x[1])[1]:
            if idx==m:
                print(result)
                break
            else:
                result+=1
                queue.popleft()
        else:
            queue.append(queue.popleft())