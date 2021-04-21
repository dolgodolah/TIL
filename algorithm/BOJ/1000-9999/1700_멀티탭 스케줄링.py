# cpu 스케줄링같은 느낌으로 풀었다.
# 멀티탭 구멍이 남아있을 경우에는 그냥 플러그를 꽂으면 되고,
# 멀티탭 구멍이 남아있지 않을 경우에는
# 멀티탭에 꽂혀있는 플러그 중에서 가장 나중에 사용될 플러그를
# 멀티탭에서 제거해주는 과정을 그대로 구현해주면 된다.
# multitap에서 plug를 찾는 과정은 시간효율을 위해 set구조를 이용했다.

from collections import deque
n,k=map(int,input().split())
plugs=deque(list(map(int,input().split())))
multitap=set()
answer=0
while plugs:
    plug = plugs.popleft() # 주어진 순서대로 플러그를 꽂는다.
    # if plug in multitap: 해당 플러그가 이미 꽂혀있는 경우는 넘어간다.

    if not plug in multitap: # 해당 플러그를 꽂아야 하는데
        if len(multitap)==n: # 멀티탭이 꽉 차있는 경우
            answer+=1 # 멀티탭에서 플러그 하나를 빼야한다.

            unused_plugs=multitap.copy()  # 멀티탭에 꽂힌 플러그 중에 제거해도 되는 unused_plugs(앞으로 사용되지 않는 플러그들)을 생성한다.
            for i in range(len(plugs)): # 앞으로 꽂아야하는 plugs을 순서대로(먼저 꽂아야할 플러그부터) 탐색하며 unused_plugs에서 plugs[i]를 제거해 나간다.
                if len(unused_plugs)<=1:
                    break
                if plugs[i] in unused_plugs:
                    unused_plugs.remove(plugs[i])

                # 첫 풀이에서 break의 위치를 여기로 해서 오답처리가 됐다.
                # unused_plugs.remove()를 먼저 실행하여 unused_plugs가 비어버리게 되면
                # 멀티탭에서 플러그를 제거하는 다음 과정이 없기때문에 오답이 발생했다.
                # if len(unused_plugs)<=1:
                #     break

            # 최종적으로 구해진 unused_plugs 중에서 pop()을 통해 나온 플러그를 멀티탭에서 제거하고, 새로운 plug를 꽂는다.
            multitap.remove(unused_plugs.pop())
            multitap.add(plug)
        else:
            multitap.add(plug)
    # print(multitap)

print(answer)
