# 21년 5월 7일 두번째 풀이
def solution(n, words):
    answer = [0,0]
    dic=dict()
    turn = 1
    idx = 0
    last_word=""
    for word in words:
        idx+=1

        # 게임 종료 조건
        if last_word and last_word[-1]!=word[0]: # 이전 단어와 끝말잇기가 안될 때
            answer=[idx,turn]
            break
        if word in dic: # 이미 나온 단어일 때
            answer=[idx,turn]
            break
    
        # 나온 단어 기록
        else: 
            dic[word]=1
            last_word=word
        
        # turn 갱신
        if idx==n:
            turn+=1
            idx=0
    
    return answer
print(solution(5,["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"]))
print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))


# 21년 1월 27일 첫번째 풀이
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
