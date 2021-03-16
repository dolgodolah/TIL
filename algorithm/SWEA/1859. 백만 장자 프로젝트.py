

#첫번째 풀이(2024ms) : deque를 이용하여 현재 리스트 중 최대값이 나올 때까지 수익이 발생한다.
# 최대값이 pop될 경우에는 남은 리스트 중에 다시 최대값을 구하고 위 과정을 반복한다.
from collections import deque
T=int(input())
for t in range(1,T+1):
    n=int(input())
    ls=list(map(int,input().split()))
    queue=deque(ls)
    max_v=max(queue)
    answer=0
    while queue:
        value=queue.popleft()
        if value==max_v and queue:
            max_v=max(queue)
        else:
            answer+=max_v-value
    print(f"#{t} {answer}")

# 두번째 풀이(1443ms) : 첫번째 풀이와 같은 아이디어지만 deque를 이용하지 않았다. 처음 입력받은 ls를 reverse시키고
# max_v(최대값)을 0으로 초기화하고 최대값보다 큰 값이 나올때까지 수익이 발생한다.
T=int(input())
for t in range(1,T+1):
    n=int(input())
    ls=list(map(int,input().split()))
    max_v=0
    answer=0
    ls.reverse()
    for value in ls:
        if value>max_v:
            max_v=value
        else:
            answer+=max_v-value
 
    print(f"#{t} {answer}")