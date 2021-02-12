# last에 최근에 탐색했던 문자를 집어넣어
# word[i]와 같으면, 즉 연속된 문자면 continue
# 처음 나오는 문자면 dic에 추가하고 last=word[i]로 갱신
# 나왔던 문자면(연속되지않는) break한다.
# break에 걸리지않고 무사히 통과하면 answer+1해준다.

n=int(input())
answer=0
for i in range(n):
    word = input()
    dic = dict()
    dic[word[0]]=1

    last = word[0]
    for i in range(1,len(word)):
        if last==word[i]:
            continue
        if not word[i] in dic:
            dic[word[i]]=1
            last=word[i]
        else:
            break
    else:
        answer+=1
print(answer)
            