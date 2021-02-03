# for-else 문법을 사용하여 해당 조합의 합이 소수가 아니라면 break, 소수이면 answer+1한다.
from itertools import combinations
def solution(nums):
    answer = 0

    for i in combinations(nums,3):
        sum_v = sum(i)
        for j in range(2,sum_v):
            if sum_v%j==0:
                break
        else:
            answer+=1


    return answer

print(solution([1,2,7,6,4]))