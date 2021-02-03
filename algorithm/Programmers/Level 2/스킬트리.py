# 어렵지 않게 풀었는데 새로운 문법을 공부해서 적어본다.
# 파이썬에서는 for - else 문법을 제공하여 for문이 break에 걸리지않고 끝까지 수행될 시 else문을 수행한다.


def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        idx=0 #배울 선행스킬의 차례를 알려주는 인덱스
        for i in skill_tree:
            if i in skill and skill[idx]!=i: #해당 스킬 i가 선행스킬 중에 있는데, 배워야할 선행스킬이 아니면 그만한다.
                break
            if i in skill and skill[idx]==i: #해당 스킬 i가 선행스킬 중에 있는데, 배워아햘 차례가 맞으면 idx+1시켜 다음 선행스킬을 가르키도록 한다.
                idx+=1
        else:
            answer+=1
            
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))

