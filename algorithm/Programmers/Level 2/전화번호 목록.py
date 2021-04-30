# 1차 풀이
# for i in phone_book:
#     for j in phone_book:
#         if i!=j and i==j[:len(i)]:
#             answer=False
#             break
#     if answer==False:
#         break

# 1차 풀이도 효율성테스트까지 다 통과되는데 2차 풀이가 훨씬 더 보기좋은 소스코드인것같다.
# 1차 풀이의 경우 i='1234', j='123'일때 j[:len(i)]를 해도 인덱싱에러가 뜨지않는다..(j의 길이보다 len(i)가 크지만 j의 최대길이만큼 가르킨다)
# 2차 풀이가 다른 언어에서도 가능한 풀이같다.
# 문자열들로 이루어진 리스트를 정렬하면 알파벳(사전)순으로 정렬이 된다.
# ['b','aa','a'] -> ['a','aa','b']
# ['123','12','3'] -> ['12','123','3']
# 즉 phone_book[i]와 phone_book[i+1]끼리 비교해주면 된다.

# 2차 풀이
def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1][:len(phone_book[i])]: #접두어이므로 len(phone_book[i])까지 탐색한다.
            answer=False
            break
    return answer


# 해시를 이용한 풀이
def solution(phone_book):
    answer = True
    dic=dict()
    for phone_number in phone_book:
        if not phone_number in dic:
            dic[phone_number]=1
    

    # phone_number가 "1195524421" 일 때를 보자.
    # number는 "1", "11", "119" ... 가 될 것이다.
    # number가 "119"일 때 if number in dic 조건에서 참이 되므로 answer는 False가 된다.
    # 주의할 점은 {"119":1 , ...}에서 자기 자신을 참으로 하는 경우를 제외해야하므로
    # number!=phone_number를 추가해준다.
    for phone_number in phone_book:
        number=""
        for i in phone_number:
            number+=i
            if number in dic and number!=phone_number:
                answer=False


    return answer
