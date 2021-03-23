#연산자 끼워넣기(2)를 풀어보고 다시 풀어봤다.
#원래 풀었던 소스하고 다른 점은 permutations가 아닌 백트래킹을 이용했다는 점이다.

import sys
input = sys.stdin.readline
n=int(input())
nums=list(map(int,input().split()))
operators=list(map(int,input().split())) #+,-,*,/

def dfs(cnt,result):
    global max_answer
    global min_answer
    if cnt==n-1:
        max_answer=max(result,max_answer)
        min_answer=min(result,min_answer)
        return
    
    if operators[0]>0:
        operators[0]-=1
        dfs(cnt+1,result+nums[cnt+1])
        operators[0]+=1
    if operators[1]>0:
        operators[1]-=1
        dfs(cnt+1,result-nums[cnt+1])
        operators[1]+=1
    if operators[2]>0:
        operators[2]-=1
        dfs(cnt+1,result*nums[cnt+1])
        operators[2]+=1
    if operators[3]>0:
        operators[3]-=1
        if result<0:
            result=abs(result)//nums[cnt+1]*(-1)
            dfs(cnt+1,result)
        else:
            dfs(cnt+1,result//nums[cnt+1])
        operators[3]+=1
max_answer=int(-10e9)
min_answer=int(10e9)
dfs(0,nums[0])
print(max_answer)
print(min_answer)



# import sys
# from itertools import permutations
# input = sys.stdin.readline
# n = int(input())
# nums = list(map(int,input().split()))
# temp = list(map(int,input().split()))
# operators = []
# for i in range(len(temp)):
#     for _ in range(temp[i]):
#         if i==0:
#             operators.append('+')
#         elif i==1:
#             operators.append('-')
#         elif i==2:
#             operators.append('*')
#         elif i==3:
#             operators.append('/')
# def calc(nums,operators):
#     num1 = nums[0]
#     for i in range(1,n):
#         if operators[i-1]=='+':
#             num1 += nums[i]
#         elif operators[i-1]=='-':
#             num1 -= nums[i]
#         elif operators[i-1]=='*':
#             num1 *= nums[i]
#         elif operators[i-1]=='/':
#             if num1<0:
#                 num1 = -1*((-1*num1)//nums[i])
#             else:
#                 num1 = num1//nums[i]
#     return num1
# sub_answer = []
# for i in permutations(operators,n-1):
#     i = list(i)
#     sub_answer.append(calc(nums,i))
# print(max(sub_answer))
# print(min(sub_answer))