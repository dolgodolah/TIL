# 번호를 사전순으로 정렬을 하게 되면 i번째 번호와 i+1번째 번호끼리
# 비교를 하여 문제에서 말하는 일관성을 확인할 수 있다.
# i번째 번호가 i+1번째 번호와 일관성이 유지된다면 그 다음 번호들과의 일관성도 유지되기 때문이다.

import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    nums=list()
    for _ in range(N):
        nums.append(input().strip())
    nums.sort()
    for i in range(len(nums)-1):
        # print(nums[i],nums[i+1][:len(nums[i])])
        if nums[i]==nums[i+1][:len(nums[i])]:
            print("NO")
            break
    else:
        print("YES")

