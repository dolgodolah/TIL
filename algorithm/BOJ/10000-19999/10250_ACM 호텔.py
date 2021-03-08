# 수학적으로 간단한 규칙만 찾으면 풀 수 있는 문제이다.
# 새로 배운건 str().zfill()이다. 예전에는 5라는 숫자를 05로 표현하려고 if(len(num))==1:'0'+num 를 해줬다.
# '5'.zfill(2)를 하면 5-> 05, '5'.zfill(5)를 하면 5->00005 식으로 0을 채워준다. 'a'.zfill(2)는 a->0a가 된다.
t=int(input())
for _ in range(t):
    h,w,n=map(int,input().split())
    answer=''

    if n%h==0:
        answer+=str(h)
    else:
        answer+=str(n%h)

    if n%h==0:
        answer+=str(n//h).zfill(2)
    else:
        answer+=str(n//h+1).zfill(2)

    print(answer)
