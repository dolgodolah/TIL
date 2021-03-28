from collections import deque
n,w,l=map(int,input().split())
trucks=deque(list(map(int,input().split())))
bridge=deque([0]*w)

answer=0
while trucks:
    bridge.popleft()
    if sum(bridge)+trucks[0]<=l:
        bridge.append(trucks.popleft())
    else:
        bridge.append(0)
    answer+=1
answer+=w
print(answer)
