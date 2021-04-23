# 2021년 4월 23일 두번째 풀이

def solution(s):
    answer = int(10e9)
    for size in range(1,len(s)//2+1):
        text="" # 해당 size로 압축된 후의 문자열
        cnt=1 # 압축 시 해당 문자의 반복 횟수(압축되는 문자 갯수)
        
        idx=0
        while idx<len(s):
            # 해당 size 기준으로 i,i+size가 같은지 확인한다.
            
            # 압축 가능
            if s[idx:idx+size]==s[idx+size:idx+size+size]:
                cnt+=1  # 압축되는 문자 갯수를 누적한다.
                idx+=size # 다음 인덱스를 size만큼 이동시켜야한다.
                
            # 압축 불가능
            else:
                # 압축 불가능한 경우는 두 가지가 있다.
                if cnt>1: # 앞에서 압축이 일어난 경우 aaa -> 3a
                    text+=str(cnt)+s[idx:idx+size] # 문자 반복 횟수를 붙여준다.
                    
                else: # 앞에서 압축이 일어나지 않은 경우 abc -> abc
                    text+=s[idx:idx+size]
                    
                cnt=1 # 문자 반복 횟수를 다시 1로 초기화한다.
                idx+=size # 다음 인덱스는 항상 +size 이다.
        # print(text)
        answer=min(len(text),answer)
    if answer==int(10e9):
        answer=1
    return answer







#2021년 1월 23일 풀이
#문자열은 제일 앞부터 정해진 길이만큼 잘라야 합니다. 따라서 주어진 문자열을 x / ababcdcd / ababcdcd 로 자르는 것은 불가능 합니다.
#위 조건을 생각안하고 하다가 머리 깨질뻔했다. 
#예를 들어 abcdef에서 압축 단위가 2일 때 ab를 검사하면 cd, ef 이렇게 검사하면된다.
#위 조건 생각 안하고 하다가 검사 순서가 ab,bc,cd,de,ef인줄 알았다. 그러므로 압축단위는 최대 문자길이/2이다.

def solution(s):
    answer = int(10e9)
    for size in range(1,len(s)//2+1): # size=문자열 압축 단위, 최대 압축 단위는 s길이/2이다.
        text = ''
        idx=0
        cnt=0
        while idx+size+size<=len(s): #indexError를 해결하기 위해 가장 수가 큰 idx+size+size가 범위를 벗어나지 않을때까지만 반복한다.

            #해당 인덱스 문자와 다음 인덱스 문자가 압축이 가능하다면
            #압축단위만큼 인덱스를 이동시키고 압축횟수를 누적한다.
            if s[idx:idx+size]==s[idx+size:idx+size+size]: 
                cnt+=1
                idx+=size 

            #압축이 불가능하다면 2가지 경우가 있다.
            #압축해온 문자가 있거나(cnt>0), 압축한 문자가 하나도 없거나(cnt==0)
            else:
                if cnt==0:
                    text+=s[idx:idx+size] #압축해온 문자가 없다면 그 문자만 붙인다. 
                else:
                    text+=str(cnt+1)+s[idx:idx+size] #압축해온 문자가 있다면 cnt+1 숫자를 앞에 붙여준다.
                idx+=size #다음 인덱스로 이동한다.
                cnt=0 #압축횟수도 0으로 초기화한다.

        #여기가 중요하다. 앞에서 indexError 처리를 위해
        #문자열 s를 다 처리하기 전에 검사가 끝나게 된다. 

        if cnt==0: #압축해온 문자가 없으면 검사못한 문자들 싹 다 추가하면 된다.
            text+=s[idx::] #aabbaccc, 압축단위3을 생각해보자. 문자 'bac'를 가르키는 idx=3에서 검사가 끝나버린다.(남은 문자가 'cc'라서 검사를 더하면 인덱스오류니까)
                            #그러므로 해당 idx=3부터 나머지 싹 다 추가하면된다.

        else: #압축해온 문자가 있다면 해당 문자 압축하고 나머지 문자 싹 다 추가하면 된다.aabaabcc
            text+=str(cnt+1)+s[idx::] #aabaabcc, 압축단위3을 생각해보자. 문자 'aab'가 압축되어 cnt=1인 상태이다.
                                        #idx=3에서 검사가 끝나버리는데 해당 문자를 압축하여 2가 앞에 붙고 idx=3부터 검사못한 문자 싹 다 추가하면
                                        #2aabcc가 된다.
        # print(size,text)
        # print()
        answer = min(answer,len(text))
    if answer==int(10e9):
        answer=1
    return answer

print(solution("aabaabcc"))
