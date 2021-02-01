# 정말 쉬운 문제를 정말 어렵게 설명해놨다. 파이썬에서는 정~말 쉬운 문제다.
# 일단 새로 배운 점은 파이썬의 sort는 안전정렬이다(같은 값일 경우 인덱스가 보장된다).
# 각 파일명들을 head,number,tail로 나누어 리스트화 시킨다.
# 예를 들어 img1.png의 경우 ['img','1','.png']가 되는 것이다.
# 모든 파일명들을 이와같이 리스트화 시킨 후에 파이썬 기본 라이브러리에 있는 sort만 하면 끝이다.

# 주어진 조건 : '대소문자 구분을 하지 않는다.', '9 < 10 < 0011 < 012 < 13 < 014 순으로 정렬된다. 숫자 앞의 0은 무시되며, 012와 12는 정렬 시에 같은 같은 값으로 처리된다.'
# 위 조건을 만족시키기 위해서 key=lambda x:(x[0].lower(),int(x[1]))를 해준다.   int(0011) -> 11
# head부분과 number부분도 같을 경우 입력에 주어진 순서를 유지한다한 조건은 파이썬의 안전정렬때문에 고려해주지 않아도 된다.
def solution(files):
    answer = []
    head = []
    number = []
    tail = []
    for file_name in files:
        for idx in range(len(file_name)):
            if file_name[idx] in ['0','1','2','3','4','5','6','7','8','9']: #해당 파일명에서 처음으로 숫자 부분이 나오면
                head.append(file_name[:idx]) #그 인덱스 전까지는 문자였기 때문에 head에 담는다.
                break
        for idx2 in range(idx,len(file_name)): #head에 담은 idx 이후로 또 검사를 한다.
            if not file_name[idx2] in ['0','1','2','3','4','5','6','7','8','9']: #숫자가 아닌 부분이 나오면
                number.append(file_name[idx:idx2]) #그 인덱스 전까지 숫자였기 때문에 number에 담는다.
                break
        else: #숫자가 아닌 부분이 나오지 않으면 즉, tail에 (빈 문자열)을 담게 될 경우에는
            number.append(file_name[idx:idx2+1]) #위 for문에서 number에 숫자를 못담았으므로 예외적으로 담아준다.
            idx2+=1 #tail에는 (빈문자열)을 담기 위해
        tail.append(file_name[idx2::]) #나머지는 tail에 담는다.

    temp = []
    for i in range(len(files)):
        temp.append([head[i],number[i],tail[i]]) #head,number,tail로 분리됐던 파일명을 같은 인덱스로 하여 temp에 담는다.
    #[['img', '12', '.png'], ['img', '10', '.png'], ['img', '02', '.png'], ['img', '1', '.png'], ['IMG', '01', '.GIF'], ['img', '2', '.JPG']]
    temp = sorted(temp,key=lambda x:(x[0].lower(),int(x[1]))) #위와 같은 temp를 정렬한다.

    for i in temp:
        answer.append(''.join(i)) #정렬된 temp를 다시 하나의 파일명으로 합쳐 answer에 추가한다.

    return answer

print(solution(['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']))
# print(solution(['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']))
# print(solution(['foo9.txt','foo010bar020.zip','F-15']))

