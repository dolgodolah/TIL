# 문자열에 대해 처리하고 해당 문자를 딕셔너리에 넣어 주어진 조건에 맞게 구현했다.

from itertools import combinations
def solution(orders, course):
    answer = []
    
    #orders를 정렬된 리스트로 바꾼다.
    for i in range(len(orders)):
        orders[i]=sorted(list(orders[i]))

    for i in course: #코스 수마다 가장 많이 나온 조합에 대해서 찾는다.
        dic=dict()
        for order in orders:
            #해당 주문에서 요리 i개들의 조합, combinations('ACDE',2) -> AC,AD,AE,CD,CE,DE
            for j in combinations(order,i): 
                temp = ''.join(j) 
                #해당 조합(temp)이 나온 횟수를 갱신한다.
                if temp in dic: 
                    dic[temp]+=1
                else:
                    dic[temp]=1
        
        #'만약 가장 많이 함께 주문된 메뉴 구성이 여러 개라면, 모두 배열에 담아..' 에 대한 처리를 위해
        #최대 주문 횟수를 구해놓고 dic을 검사해 최대 주문 횟수와 같은 조합을 answer에 추가한다.
        if dic: #해당 course에 대한 조합이 없을 때 예외처리
            max_v=dic[max(dic,key=lambda x:dic[x])]
        for k in dic:
            if dic[k]==1: #최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만.. 에 대한 예외처리
                continue
            if dic[k]==max_v: 
                answer.append(k)
    answer = sorted(answer)
    return answer

# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
# print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))