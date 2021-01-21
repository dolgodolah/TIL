# itertools 라이브러리를 이용한 풀이와 dfs 백트래킹을 이용해 직접 조합을 구한 풀이다.

from itertools import combinations
def solution(numbers):
    answer = set()
    for i in combinations(numbers,2):
        answer.add(sum(i))
    answer = sorted(list(answer))
    return answer

# def dfs(cnt,idx,numbers,ls,answer):
#     if cnt==2:
#         answer.add(sum(ls))
#         return
#     for i in range(idx,len(numbers)):
#         ls.append(numbers[i])
#         dfs(cnt+1,i+1,numbers,ls,answer)
#         ls.pop()

# def solution(numbers):
#     answer = set()
#     ls = []
#     dfs(0,0,numbers,ls,answer)
#     answer = sorted(answer)
#     return answer

# print(solution([2,1,3,4,1]))