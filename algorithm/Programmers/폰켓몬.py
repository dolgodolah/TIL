from itertools import combinations
def solution(nums):
    answer = 0
    n = len(nums)//2 #고를 수 있는 폰켓몬의 수
    nums = set(nums) #폰켓몬의 종류를 나타내게끔 바꿔준다.

    if n>len(nums): #고를 폰켓몬의 수가 폰켓몬의 종류보다 많으면 최대값은 폰켓몬의 종류수이다.
        answer=len(nums)
    elif n<=len(nums): #고를 폰켓몬의 수보다 폰켓몬의 종류가 크거나 같으면 최대값은 폰켓몬의 모든 종류를 다 가져갈 수 있다.
        answer=n
    return answer

print(solution([3,1,2,3]))