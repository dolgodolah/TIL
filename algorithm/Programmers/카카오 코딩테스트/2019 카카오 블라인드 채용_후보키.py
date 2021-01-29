#배운거밖에 없었던 문제였다. 

# relation에 있는 값을 한번에 여러 개 가져와야했다.
# 1. 리스트의 여러 인덱스에 있는 값 가져오는 방법
#   - 튜플을 이용하면 된다. ls=[9,8,7,6,5,4]일 때
#   - [ls[index] for index in (1,3)]이면 1,3번 인덱스에 있는 리스트 값(8,6)을 불러와 리스트[8,6]로 만든다.

# 문제 조건 중 최소성 만족을 위해서는 교집합의 성질을 이용해야했다.
# 2. 교집합, 합집합 구하는 방법
#   - 교집합은 {}.intersection({}) 혹은 &
#   - 합집합은 {}.union({}) 혹은 |

# 3. set의 값을 제거하는 방법에는 remove와 discard가 있다.
#   - remove는 해당 값이 없으면 error 발생 
#   - discard는 해당 값이 없어도 진행
from itertools import combinations
def solution(relation):
    answer = 0
    row = len(relation)
    col = len(relation[0])

    # 조합 가능한 후보키들을 구한다.
    candidates = []
    for i in range(1,col+1):
        for j in combinations(range(col),i):
            candidates.append(j)
    # print(candidates)
    
    #후보키 조합들 중에서 유일성을 만족하는 후보키들을 temp_answer에 추가한다.
    temp_answer=[]
    for candidate in candidates:
        
        temp=set()
        for item in relation:
            temp.add(tuple([item[key] for key in candidate]))
        if len(temp)==row:
            temp_answer.append(candidate)
    

    #유일성을 만족하는 후보키들 중 최소성을 만족하지 못하는 후보키들을 버린다.(discard)
    #[(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
    #discard와 &(intersection,교집합)을 사용하기 위해서는 set이어야한다.
    temp = set(temp_answer)
    for i in range(len(temp_answer)):
        for j in range(i+1,len(temp_answer)):
            if len(temp_answer[i])==len(set(temp_answer[i])&(set(temp_answer[j]))): #후보키 temp_answer[j]는 temp_answer[i] 없으면 안돼! 이 느낌이다. 즉 최소성을 만족하지 못한다는 소리.
                temp.discard(temp_answer[j])

    answer = len(temp)
    return answer


print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))
