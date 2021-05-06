# 처음엔 queue=[0]*bridge_length만큼 생성하여 queue 하나로만 해결하려 했으나 시간초과가 발생한다.
# 실제로 다리를 지나고 있는 트럭이 한 대여도 [8,0,0,0,0,...,0] 와 같이 다리 길이만큼 sum(queue)를 해주기 때문에이다.

# 시간복잡도와 공간복잡도는 반비례한다. weigth_queue와 sec_queue를 따로 만들어 
# weight_queue에는 다리를 지나는 트럭들의 무게를, sec_queue에는 다리를 지나는 트럭들의 경과시간을 기록한다.
# 둘의 길이는 같으므로 sec_queue의 길이만큼 탐색하면서 경과시간을 갱신하며 bridge_length보다 커지면 두 queue에서 pop해준다.
# sum(weigth_queue)의 경우도 실제 다리를 지나고 있는 트럭의 개수만큼만 연산을 하므로 시간복잡도에서 훨씬 효율적이다.
from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights=deque(truck_weights) # 다리를 건너야하는 트럭
    weight_queue = deque() # 다리를 건너고 있는 트럭들의 무게
    sec_queue = deque() # 다리를 건너고 있는 트럭들의 경과 시간

    while truck_weights or weight_queue: # 모든 트럭이 다리를 지날 때까지 반복
        answer+=1
        # 다리 길이만큼 이동한 트럭들을 확인한다.
        for _ in range(len(sec_queue)):
            sec=sec_queue.popleft()
            value=weight_queue.popleft()
            if sec+1<=bridge_length:
                sec_queue.append(sec+1)
                weight_queue.append(value)

        if truck_weights and sum(weight_queue)+truck_weights[0]<=weight:
            weight_queue.append(truck_weights.popleft())
            sec_queue.append(1)

    return answer

print(solution(100,100,[10,10,10]))
