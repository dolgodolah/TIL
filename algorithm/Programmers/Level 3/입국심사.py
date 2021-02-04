# 이분탐색으로 문제가 분류돼있기도 하고,
# 제한사항에서 데이터 범위를 보면 이분탐색이라는건 쉽게 알 수 있다.
# 문제는 뭘 이분탐색할 것인가? 이다.
# 입국심사 기다리는 사람(n)이 1이상 1,000,000,000이하
# 각 심사관이 한 명 심사하는데 걸리는 시간(times[i])이 1이상 1,000,000,000 이하
# 이 둘중 이분탐색을 해야할 것 같은데 도저히 엄두가 안난다.
# 해답은 '심사관들에게 주어질 시간'을 이분탐색 하는 것이다.
# left를 1분, right를 최댓값인 max(times)*n를 준다.(가장 오래걸리는 심사관이 모든 인원을 다 검사하는 경우)
# solution(6,[7,10]) 일 때 mid = (left+right)//2 = 30을 예로 들어보자. 심사관들에게 30분이라는 시간이 주어졌다.
# 첫번째 심사관은 4명을 심사할 수 있고, 두번째 심사관은 3명을 심사할 수 있다. 총 7명을 심사할 수 있는데
# 이 값은 6보다 크므로 더 줄일 수 있는 가능성이 있다. 이처럼 이분탐색을 진행하면 된다.

def solution(n, times):
    answer = 0
    left = 1
    right = max(times)*n
    while left<=right:
        mid = (left+right)//2
        cnt = 0
        for time in times:
            cnt+=mid//time
        if cnt>=n:
            right=mid-1
            answer=mid
        elif cnt<n:
            left=mid+1
    return answer


print(solution(6,[7,10]))