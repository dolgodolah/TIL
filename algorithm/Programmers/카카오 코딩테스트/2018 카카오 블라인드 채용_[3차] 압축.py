# 문제 이해하는데 약-간의 시간이 걸렸다.
# 어느정도 이해하고 주어진 조건(과정)에 맞춰 하나씩 구현하고
# 나름대로 다 구현하고 테스트차원으로 실행해봤는데 바로 정답이 출력된다.
# 디버깅이 습관이 됐는데 한번에 통과해버리니까 오히려 더 의심스럽다.

def solution(msg):
    answer = []
    msg = list(msg) # 색인번호 출력 후 msg에서 해당 문자를 지우기 위해서 리스트화 시킨다.
    dictionary = ['','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] # 길이가 1인 모든 단어를 사전에 초기화한다.
    i = 0
    while msg: # 입력이 처리되지 않은 글자가 남아있을때까지 수행
        if ''.join(msg[:len(msg)-i]) in dictionary: # 입력 문자 중에 가장 긴 문자열부터 사전에서 찾아본다.
            w=''.join(msg[:len(msg)-i])
            answer.append(dictionary.index(w)) # w에 해당하는 사전의 색인번호를 출력한다.
            for _ in range(len(w)): # msg에서 w를 제거한다. (w의 길이만큼 앞에서부터 제거했다.)
                msg.pop(0)
            if msg: # 입력(msg)에서 처리되지 않은 다음 글자가 남아있다면(c),
                dictionary.append(w+msg[0]) # w+c에 해당하는 단어를 사전에 등록한다.
            i=0
        else:
            i+=1
    return answer

print(solution('KAKAO'))
print(solution('TOBEORNOTTOBEORTOBEORNOT'))
