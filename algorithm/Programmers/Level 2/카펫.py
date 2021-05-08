# 21년 5월 7일 두번째 풀이
def solution(brown, yellow):
    answer = []

    # 노란 격자의 행을 1부터 증가시켜보자.
    for i in range(1,yellow+1):
        if not yellow%i==0: #  격자의 행과 열의 곱이 노란 격자 갯수가 될 수 없을 때
            continue
        
        
        row=i+2 # 노란 격자의 행 갯수+2가 카펫의 행 갯수가 된다.
        column=yellow//i+2 

        if row*2+(column-2)*2==brown:
            answer=[column,row]
            break

    return answer

print(solution(24,24))


# 21년 1월 25일 첫번째 풀이
# yellow의 개수를 이용해 yellow 가로가 1일때부터 오름차순으로 완전탐색했다.
# 

def solution(brown, yellow):
    answer = []
    for i in range(1,yellow+1):
        height = i
        if not yellow%i==0: # yellow가 24일 때 i(세로길이)가 5이면 가로길이가 정수로 나오지 않으므로 넘어간다.
            continue
        width = yellow//i # yellow의 세로길이가 i일때 가로길이를 구한다.
        #해당 height, width일 때 brown의 개수를 구한다.(height*2+(width+2)*2)
        if height*2 + (width+2)*2==brown: #주어진 brown의 개수와 같으면
            answer=[width+2,height+2] #정답을 갱신하고 break한다.
            break #가로길이가 세로길이보다 길어야하므로 더 진행하면 세로길이가 더 길 때까지 진행된다.
    return answer

print(solution(10,2))
print(solution(8,1))
print(solution(24,24))