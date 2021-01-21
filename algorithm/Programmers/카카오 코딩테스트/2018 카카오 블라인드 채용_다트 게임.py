# 문자열에 대한 구현 문제이다. idx를 통해 dartResult의 내용을 탐색한다.
# 주어진 조건과 예외적인 케이스에 대해 빨리 캐치하고 구현을 해야한다.
# 고려를 해줬던 예외적인 부분은 점수(숫자)가 '10'인 경우(문자열의 두자리를 차지)와
# 스타상(*)이 전에 얻은 점수도 2배 해주는 경우, 요종도?

def solution(dartResult):
    temp=0 #해당 스테이지에서 얻은 점수에 대한 값
    idx=0 #dartResult 문자열을 가르키는 변수
    score = [] #다음 스테이지로 넘어가면 전 스테이지에서 얻은 temp의 값을 score에 삽입시킨다.
    while idx<len(dartResult):
        if dartResult[idx] in ['0','1','2','3','4','5','6','7','8','9']: #숫자를 가르키면
            if temp!=0:score.append(temp) #전 스테이지에서 얻은 점수를 score에 삽입한다. (첫 스테이지의 경우는 무시한다.)
            if dartResult[idx+1]=='0': #정수가 10인 경우
                temp=int(dartResult[idx]+dartResult[idx+1]) #int형 10을 temp에 저장
                idx+=1 #'10'이 문자열 두자리를 차지하므로 idx를 1증가
            else: #0~9인 경우
                temp=int(dartResult[idx]) #int형 0~9를 temp에 저장

        elif dartResult[idx] in ['S','D','T']:
            if dartResult[idx]=='S': #해당 점수 1제곱
                temp=temp**1
            elif dartResult[idx]=='D': #해당 점수 2제곱
                temp=temp**2
            elif dartResult[idx]=='T': #해당 점수 3제곱
                temp=temp**3

        elif dartResult[idx] in ['#','*']:
            if dartResult[idx]=='#': #해당 점수 마이너스
                temp=-temp
            elif dartResult[idx]=='*': #스타상(*)이 첫번째 기회에 나올 경우 전에 얻는 점수가 없기 때문 예외처리를 해줘야한다.
                if score: #전에 얻은 점수가 있을 때만
                    score[-1]*=2 #바로 전에 얻은 점수와 
                temp*=2 #해당 점수를 각 2배해준다.
        idx+=1

    #temp에 계산된 점수를 score에 저장하는 타이밍이 다음 숫자(0~10)을 만날때인데
    #마지막 스테이지는 마지막 숫자이기 때문에 마지막 temp(점수)를 추가해준다.
    score.append(temp)
    return sum(score)

print(solution('1D2S0T'))
