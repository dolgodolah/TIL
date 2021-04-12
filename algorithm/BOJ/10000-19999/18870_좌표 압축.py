# 정렬, 해쉬(딕셔너리)를 활용하는 문제이다.
# 일단 기본 아이디어는 오름차순 정렬이다.
# [2, 4, -10, 4, -9] -> [-10, -9, 2, 4, 4]가 되고
# (2,4,-10,4,-9) 순서대로 정렬된 리스트에서 index를 찾으면 된다.
# 2의 인덱스는 2, 4의 인덱스는 3이 되어 [2,3,0,3,1]과 같은 답이 나온다.

# 문제는 중복된 수이다.
# [1000, 999, 1000, 999, 1000, 999] -> [999, 999, 999, 1000, 1000, 1000]가 되고
# 여기서 답을 구하면 [3,0,3,0,3,0]이 되는데 실제 답은 [1,0,1,0,1,0]이 되어야한다.
# 즉, 중복된 수들을 정렬하기 전에 없애줘야하는데 이는 sorted(set(nums))를 통해 구할 수 있다.
# [999,1000]이 구해지고 딕셔너리를 통해 인덱싱 번호를 부여해준다. {999:0, 1000:1}
# 위 예제와 같이 (1000,999,1000,999,1000,999)를 차례대로 탐색하며 인덱스를 찾는다.

import sys
input=sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
sorted_nums=sorted(set(nums))
dic=dict()
for i in range(len(sorted_nums)):
    dic[sorted_nums[i]]=i
answer=list()
for num in nums:
    answer.append(dic[num])
print(*answer)