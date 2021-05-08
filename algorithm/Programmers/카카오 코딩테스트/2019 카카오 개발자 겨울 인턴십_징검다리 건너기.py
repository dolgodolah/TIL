# 21년 5월 7일
def solution(stones, k):
    answer = 0
    left=1
    right=max(stones)
    while left<=right:
        mid=(left+right)//2
        cnt=0
        for stone in stones:
            if stone-mid<=0:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                right=mid-1
                answer=mid
                break
        else:
            left=mid+1
    return answer


# 21년 2월 11일
# 징검다리를 건너야하는 니니즈 친구들의 수를 이분탐색한다.
# 니니즈 친구들의 수를 mid라고 했을 때 stones[idx]-mid가 0보다 작을 때
# 즉 여러칸을 건너뛰어야할 때가 k번 '연속'으로 발생할 때 친구들의 수를 줄여보아 최솟값을 찾는다.
# k번 '연속'으로 발생하지 않을 때(건너는 친구들이 적다는 뜻)는 left=mid+1를 통해 친구들의 수를 추가해본다.


def solution(stones, k):
    answer = 0
    
    left=0
    right=200000000
    while left<=right:
        mid = (left+right)//2
        cnt=0
        val=False
        for stone in stones:
            if stone-mid<=0:
                cnt+=1
            else:
                cnt=0
            if cnt==k:
                val=True
                break
        if val:
            right=mid-1
            answer=mid
        else:
            left=mid+1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))