import sys
input = sys.stdin.readline
L,C=map(int,input().split())
ls=list(input().split())
ls=sorted(ls) #정렬된 문자열을 선호하는 조교들의 성향으로 미루어 보아 암호를 이루는 알파벳이 암호에서 증가하는 순서로 배열되었을 것이라고 추측된다
answer = []
def dfs(cnt,a,b,password,idx): #암호길이, 자음갯수, 모음갯수, 비밀번호, 인덱스
    global answer
    if cnt==L and a>=2 and b>=1: #암호길이가 L이고 자음이 2개이상, 모음이 1개이상일 때만 추가한다.
        print(password)
    
    for i in range(idx,C):
        if ls[i] in ['a','i','u','e','o']: #추가할 문자가 모음일때
            dfs(cnt+1,a,b+1,password+ls[i],i+1)
        else: #추가할 문자가 자음일때
            dfs(cnt+1,a+1,b,password+ls[i],i+1)

dfs(0,0,0,"",0)