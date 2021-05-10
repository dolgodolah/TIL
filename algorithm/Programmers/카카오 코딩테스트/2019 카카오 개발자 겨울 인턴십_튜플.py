# 21년 5월 6일 두번째 풀이
def solution(s):
    answer = []
    s=s.lstrip("{")
    s=s.rstrip("}")
    s=s.split("},{")
    for i in range(len(s)):
        s[i]=s[i].split(",")
    
    s.sort(key=lambda x:len(x))
    
    dic=dict()
    for i in range(len(s)):
        for j in s[i]:
            if not j in dic:
                dic[j]=1
                answer.append(int(j))
    return answer


#21년 1월 25일 첫번째 풀이
# 카카오 코딩테스트는 문자열 문제가 많이 출제되는 것 같다.

# 문제 해결 아이디어는 원소가 하나인것부터 answer에 추가하면 된다.
# 예를 들어 "{{1,2,3},{2,1},{1,2,4,3},{2}}"이라면 
# {2}에서 2를 추가하고 {2,1}에서 2는 이미 추가됐으니 1을 추가하고 쭉 진행하면 answer=[2,1,3,4]가 된다.
# [2,1,3,4]에서 {2},{1,2}는 만들어질 수 있으나 {1}, {3}는 만들어질 수 없는 성질을 이용한 것이다.

# strip 문법을 알기 전 풀이는 밑에 주석처리 해놨다.
# strip을 알기전에는 일일이 문자열을 검사하여 }와 { 그리고 ,가 나올때마다 처리를 해주어
# "{{1,2,3},{2,1},{1,2,4,3},{2}}" 문자열을 [['2'],['2','1'],['1','2','3'],['1','2','4','3']]와 같은 리스트 형태(길이기준 정렬까지)로 바꿨다.
# strip문법을 이용하면 이 과정을 쉽게 할 수 있다.
# lstrip과 rstrip으로 왼쪽과 오른족에 있는 {,}들을 벗겨주고
# },{를 기준으로 s.split('},{') 해주면 ['1,2,3', '2,1', '1,2,4,3', '2'] 로 바뀌고
# 이를 각 문자열마다 split(',')를 해주어 적절한 형태로 바꿔주면 [['2'],['2','1'],['1','2','3'],['1','2','4','3']] 가 된다.

def solution(s):
    answer = []
    s=s.lstrip('{').rstrip('}').split('},{')
    ls = []
    # print(s)
    for i in s:
        ls.append(i.split(','))
    ls.sort(key=lambda x:len(x))
    # print(ls)
    for i in ls:
        for j in i:
            j=int(j) #리스트에 저장된 형태는 str형이므로 정답 출력 형식에 맞추어 int형으로 바꾼다.
            if not j in answer:
                answer.append(j)
    return answer


# def solution(s):
#     answer = []
#     ls=[[] for _ in range(s.count('{')-1)]
#     s=s[1:-1]
#     temp=''
#     idx=0
#     for i in s:
#         if i=='{':
#             continue
#         elif i=='}':
#             ls[idx].append(temp)
#             temp=''
#             idx+=1
#         elif i==',':
#             if temp:
#                 ls[idx].append(temp)
#                 temp=''
#         else:
#             temp+=i
#     ls.sort(key=lambda x:len(x))
#     print(ls)
#     for i in ls:
#         for j in i:
#             j=int(j)
#             if not j in answer:
#                 answer.append(j)
    
#     return answer
    
print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
print(solution("{{20,111},{111}}"))