# 해결 아이디어는 쉬웠는데 시간초과가 발생했다. 
# 시간단축을 위해 여러 가지치기를 해봤는데 안된다.
# https://mungto.tistory.com/212 에서 힌트를 얻었다.
# 딕셔너리를 통해 해당 cnt번째 교환 때 이미 만들어졌던 숫자조합이면 건너뛰는거다.
def calc(ls):
    global answer
    result = 0
    weight = 10**(len(ls)-1)
    for i in range(len(ls)):
        result += int(ls[i])*(weight//10**i)
    return result
def dfs(cnt):
    global answer
    if cnt==0:
        answer = max(answer,calc(ls))
        return
    for i in range(len(ls)):
        for j in range(i+1,len(ls)):
            ls[i],ls[j]=ls[j],ls[i]
            temp = ''.join(ls)
            if not (temp,cnt-1) in dic:
                dic[(temp,cnt-1)]=1
                dfs(cnt-1)
            ls[i],ls[j]=ls[j],ls[i]


T = int(input())
for t in range(1,T+1):
    a, b = map(str,input().split())
    cnt = int(b)
    answer = 0
    ls=[]
    dic = dict()
    for i in a:
        ls.append(i)
    dfs(cnt)
    print(f"#{t} {answer}")
