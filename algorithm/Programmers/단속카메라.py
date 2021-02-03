# 진출 시간을 기준으로 오름차순 정렬을 한다.
# routes를 탐색하면서 카메라의 idx를 갱신해간다.
# 현재 카메라의 idx가 해당 route의 진입지점보다 작으면
# 카메라 idx를 새롭게 갱신해줘야 하는데 이는 해당 route의 진출지점으로 한다. (그리디)
def solution(routes):
    answer = 0
    routes.sort(key=lambda x:x[1])
    idx = -30001
    for route in routes:
        if idx<route[0]:
            idx=route[1]
            answer+=1
    return answer

print(solution([[-20,15], [-14,-5], [-18,-13], [-5,-3]]))