# permutations를 이용한 풀이와 백트래킹을 이용해 직접 순열을 구하는 풀이로 해봤다.
# ''.join(A) 여기서 A는 str로 이뤄져야하는건 알고있었는데
# int가 오더라도 ''.join(map(str,A))를 하면 된다는걸 알았다.
import sys
from itertools import permutations

n = int(input())
ls = list(input().split())


def calc(nums):
    for i in range(n):
        if ls[i]=="<":
            if not nums[i]<nums[i+1]:
                return False
        else:
            if not nums[i]>nums[i+1]:
                return False
    return True
max_answer = '0123456789'
min_answer = '9876543210'
for i in permutations(range(10),n+1):
    if calc(i):
        val = ''.join(map(str,i))
        max_answer=max(max_answer,val)
        min_answer=min(min_answer,val)
print(max_answer)
print(min_answer)
# nums = []
# max_answer = '0123456789'
# min_answer = '9876543210'
# def check(nums):
#     for i in range(n):
#         if ls[i]=="<":
#             if not int(nums[i])<int(nums[i+1]):
#                 return False
#         else:
#             if not int(nums[i])>int(nums[i+1]):
#                 return False
#     return True
# def dfs(cnt):
#     global max_answer,min_answer
#     if cnt==n+1:
#         if check(nums):
#             val = ''.join(map(str,nums))
#             max_answer=max(max_answer,val)
#             min_answer=min(min_answer,val)      
#         return
    
#     for i in range(10):
#         if not i in nums:
#             nums.append(i)
#             dfs(cnt+1)
#             nums.pop()
# dfs(0)
# print(max_answer)
# print(min_answer)

        

