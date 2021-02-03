def solution(s):
    ls = [s[0]]
    for i in range(1,len(s)):
        if ls and ls[-1]=='(' and s[i]==')':
            ls.pop()
        else:
            ls.append(s[i])
        # print(ls)
    if ls:return False
    else : return True

print(solution("()()"))
print(solution("(())()"))
print(solution(")()("))
print(solution("(()("))