# "java backend junior pizza 150"와 같은 info가 주어지면
# "java backend junior pizza 150", "- backend junior pizza 150", "java - junior pizza 150", "java backend - pizza 150", ... , "- - - pizza 150", "- - - - 150"와 같이 16개(2^4)의 조합을 만들 수 있다.
# 즉, "- backend - pizza"와 같은 쿼리가 주어지면 "java backend junior pizza 150"을 통해 만들어진 조합으로 150을 얻을 수 있다.

from itertools import combinations
from bisect import bisect_left

def solution(info, query):
    answer = []
    dic = {}

    # "java backend junior pizza 150"로 만들 수 있는 16개의 조합을 구한다.
    # "java backend junior pizza 150" -> "javabackendjuniorpizza", "-backendjuniorpizza", "java-juniorpizza" ... "---pizza", "----"
    for i in info:
        individual=i.split()
        tmp=individual[:-1] # 조합을 구하기 전에 점수 부분은 제외해준다. ['java', 'backend', 'junior', 'pizza', '150'] -> ['java', 'backend', 'junior', 'pizza]
        for i in range(5): # i는 "-"의 갯수
            for j in combinations(range(4),i): # "-"의 위치를 combinations를 통해 구한다.
                tmp_individual=tmp.copy()
                for k in j:
                    tmp_individual[k]='-'
                
                # key-value를 "javabackendjuniorpizza":[150,260] 과 같은 형태로 만든다.
                if not ''.join(tmp_individual) in dic:
                    dic[''.join(tmp_individual)]=[int(individual[-1])]
                else:
                    dic[''.join(tmp_individual)].append(int(individual[-1]))
    
    # 이분탐색을 위해 구해진 dic의 values를 정렬해준다.
    # {'javabackendjuniorpizza': [150], ..., 'javabackendjunior-': [150, 80], '-backend-pizza': [150, 260], ... , '----': [150, 210, 150, 260, 80, 50]}
    # -> {'javabackendjuniorpizza': [150], ..., 'javabackendjunior-': [80, 150], '-backend-pizza': [150, 260], ... , '----': [50, 80, 150, 150, 210, 260]}
    for value in dic.values():
        value.sort()
   
    # 주어진 query들을 탐색한다.
    for q in query:
        q=q.split()

        # 주어진 쿼리에 대한 정보가 dic에 없다면 에러가 발생하므로 dic에 있을 때만 탐색한다.
        if q[0]+q[2]+q[4]+q[6] in dic:
            ls=dic[q[0]+q[2]+q[4]+q[6]]

            # dic[q[0]+q[2]+q[4]+q[6]]=[50,80,150,150,210,260]에서 q[7]=150점 이상받은 사람은 모두 몇 명인가?
            # bisec_left([50,80,150,150,210,260], 150)을 통해 150의 인덱스를 구하고 (return 2)
            # 전체 길이에서 해당 인덱스를 빼주면 150 이상 받은 사람이 몇 명인지 구할 수 있다.
            answer.append(len(ls)-bisect_left(ls,int(q[7]))) 
                
        else:
            answer.append(0)

    return answer


print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"],["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))