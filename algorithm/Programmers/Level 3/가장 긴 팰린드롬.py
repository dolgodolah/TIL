def solution(s):
    answer = 0
    #내 풀이
    for i in range(len(s),0,-1): #가장 긴 팰린드롬을 찾기 때문에 내림차순으로 탐색하여 팰린드롬 발견 시 바로 return 한다.
        for j in range(0,len(s)):
            if i+j<=len(s): # i+j가 문자열의 길이를 벗어나지않을 때만 다음을 수행한다.
                temp = s[j:j+i] # 문자열을 리스트화 시켜 [::-1]를 통해 뒤집은 리스트와 확인한다.
                if temp==temp[::-1]:
                    return i
            else: # i+j가 문자열의 길이를 벗어나면 break하고 i를 -1한다.(길이를 줄여본다.)
                break

    # 다른 사람 풀이
    # for i in range(len(s)):
    #     for j in range(i,len(s)+1):
    #         temp = s[i:j]
    #         if temp==temp[::-1]:
    #             answer=max(answer,len(temp))
    # return answer
    


print(solution('abcdcba'))
# print(solution('abacde'))
# print(solution("a"))