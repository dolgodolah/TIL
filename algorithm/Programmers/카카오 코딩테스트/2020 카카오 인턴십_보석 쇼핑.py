# left=0, right=0에서 right를 1씩 늘려가 모든 보석을 다 샀는지 len(dic)==len(gem_type):를 통해 확인한다. 
# 모든 보석을 구매한 상태가 되면 left를 1씩 늘려가(길이를 줄여나감) 그래도 모든 보석을 다 산 상태인지 확인한다.
# 모든 보석을 다 산 상태이면 계속해서 left를 1씩 늘여 길이를 줄여보고
# 다 사지않은 상태이면 right를 1 늘린다. 즉 left,right 두 포인터를 통해 gems를 탐색한다.

# 다른 풀이들 보면 while left<len(gems) and right<len(gems):를 했는데 right<len(gems)만 해도 되자않나?
# 새로 배운게 있다면 dict의 (key,value) 한 쌍을 삭제하려면 del dic[key]를 하면된다.

def solution(gems):
    answer = []
    temp_answer = []
    gem_type = set(gems)
    left,right=0,0
    dic = dict()
    dic[gems[0]]=1
    # print(dic,len(dic))
    while right<len(gems):
        if len(dic)==len(gem_type):
            temp_answer.append((left,right))
            dic[gems[left]]-=1
            if dic[gems[left]]==0:
                del dic[gems[left]]
            left+=1 #left 포인터는 인덱싱을 하고 left+1을 하지만
        else:
            right+=1 #right 포인터는 +1을 하고 인덱싱을 하기때문에 인덱싱 에러가 뜰 수 있다.
            if right>=len(gems): #인덱싱 에러가 뜨지 않도록 해준다.
                break
            if gems[right] in dic:
                dic[gems[right]]+=1
            else:
                dic[gems[right]]=1
    min_v = int(10e9)
    for start,end in temp_answer:
        if min_v>end-start:
            min_v=end-start
            answer = [start+1,end+1]
    return answer


# print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
print(solution(["XYZ", "XYZ", "XYZ"]))