from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses=deque(progresses)
    speeds=deque(speeds)
    while progresses:
        for i in range(len(progresses)):
            progresses[i]+=speeds[i]
            
        cnt=0
        while progresses and progresses[0]>=100:
            progresses.popleft()
            speeds.popleft()
            cnt+=1
        if cnt>0:answer.append(cnt)
    return answer