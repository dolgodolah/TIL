from collections import deque
def solution(priorities, location):
    answer = 0
    priorities=deque(priorities)
    for i in range(len(priorities)):
        priorities[i]=(i,priorities[i])
    while priorities:
        idx,priority = priorities.popleft()
        if priorities and priority<max(priorities,key=lambda x:x[1])[1]: #해당 인쇄가 우선순위에서 밀려난다.
            priorities.append((idx,priority))
        else: #해당 문서가 인쇄된다.
            answer+=1
            if idx==location: #인쇄되는 해당 문서가 내가 원하는 문서일 경우
                break
    return answer