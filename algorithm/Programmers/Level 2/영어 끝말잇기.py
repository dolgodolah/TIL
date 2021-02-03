#딕셔너리를 통해 앞에서 나왔던 단어인지 체크해줬다.
#동시에 last에서 전에 나왔던 단어를 갱신해줘 끝말과 같은지 확인한다.
def solution(n, words):
    answer = []
    dic=dict()
    last = ''
    cnt=0
    turn=1
    for word in words:
        cnt+=1
        if not last:
            dic[word]=1
            last=word
        else:
            if last[-1]==word[0]:#끝말과 같고
                if not word in dic: #처음 나오는 단어이면
                    dic[word]=1
                    last=word
                else: #앞에서 나왔던 단어이면
                    answer=[cnt,turn]
                    break
                if cnt==n:
                    turn+=1
                    cnt=0
            elif last[-1]!=word[0]:
                answer=[cnt,turn]
                break
    else:
        answer=[0,0]
    return answer

print(solution(3,['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']))
