# 풀기는 풀었는데 다소 정리가 안돼있고 지저분하다. 다른 사람 풀이보면서 깔끔한 소스보고 다시 해봐야겠다.
# 일단 내 아이디어는 다음과 같다.
# banned_id마다 해당되는 user_id들을 ls에 기록했다.
# user_id가 ["frodo", "fradi", "crodo", "abc123", "frodoc"]과 같고 기록할 banned_id를 '*rodo'라고 했을 때 
# 문자열 길이가 맞지 않으면 바로 다음 user_id로 continue
# 해당 문자가 '*'일 때는 다음 인덱스로 가르키도록  continue
# 해당 문자가 일치하지 않으면 break
# 무사히 다 통과하면 ls에 추가한다.

# banned_id마다 해당되는 ls들을 구하고나면 이 ls를 가지고 dfs를 수행하여 가능한 조합들을 구한다.
# 그 조합이 이미 있는 조합이라면 answer을 추가하지 않고, 처음 나오는 조합일 때만 answer을 추가한다.

from itertools import combinations
temp = set()
answer = 0

def dfs(cnt,n,ls,new_ls):
    global answer
    if cnt==n:
        temp_ls = sorted(new_ls)
        if not tuple(temp_ls) in temp:
            temp.add(tuple(temp_ls))
            answer+=1
        return
    for i in range(cnt,n):
        for j in range(len(ls[i])):
            if not ls[i][j] in new_ls:
                new_ls.append(ls[i][j])
                dfs(cnt+1,n,ls,new_ls)
                new_ls.pop()
        break
def solution(user_id, banned_id):
    global temp
    global answer
    answer = 0
    temp = set()
    ls = [[] for _ in range(len(banned_id))]
    for i in range(len(banned_id)):
        for j in range(len(user_id)):
            if len(banned_id[i])!=len(user_id[j]):
                continue
            for k in range(len(banned_id[i])):
                if banned_id[i][k]=='*':
                    continue
                if banned_id[i][k]!=user_id[j][k]:
                    break
            else:
                ls[i].append(user_id[j])
    # print(ls)
    dfs(0,len(ls),ls,[])
    return answer

# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"]))
# print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["*rodo", "*rodo", "******"]))
print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "*rodo", "******", "******"]))
