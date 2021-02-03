# 최소값을 구하는 문제에서는 시간 단축을 위해서 bfs를 이용하도록 하자!

#bfs 풀이
from collections import deque
def solution(begin, target, words):
    answer = 0
    def check(x,word):
        cnt=0
        for i in range(len(x)):
            if x[i]!=word[i]:
                cnt+=1
        if cnt==1:
            return True
        else:
            return False
    def bfs():
        queue=deque()
        queue.append((begin,0))
        visited = [False]*len(words)
        while queue:
            x,cnt = queue.popleft()
            if x==target:
                return cnt
            for i in range(len(words)):
                if check(x,words[i]) and visited[i]==False:
                    visited[i]=True
                    queue.append((words[i],cnt+1))
        return 0

    answer = bfs()
    return answer

#dfs풀이
# answer = int(10e9)
# def solution(begin, target, words):
#     global answer
#     answer = int(10e9) #solution 함수가 호출될때마다 answer을 초기값으로 초기화해준다.
#     if not target in words:
#         return 0
    
#     def check(a,b):# 한 개의 알파벳만 바꿀 수 있으므로 a단어가 b단어와 몇 개가 다른지 체크한다.
#         cnt = 0
#         for i in range(len(a)):
#             if a[i]!=b[i]:
#                 cnt+=1
#         if cnt==1:
#             return True
#         else:
#             return False
    
#     def dfs(result,cnt):
#         global answer
#         if result==target:
#             answer = min(answer,cnt)
#             return
#         for i in range(len(words)):
#             if check(result,words[i]) and visited[i]==False:
#                 visited[i]=True
#                 dfs(words[i],cnt+1)
#                 visited[i]=False
#     visited = [False]*len(words)
#     dfs(begin,0)
#     return answer

print(solution('hit','cog',['hot', 'dot', 'dog', 'lot', 'log', 'cog']))
# print(solution('hit','hot',['hot', 'dot', 'dog', 'lot', 'log']))
# print(solution('hit','cog',['cog', 'log', 'lot', 'dog', 'dot', 'hot']))