#21년 5월 6일 풀이
def solution(n,a,b):
    answer=1
    while True:
        # 해당 라운드에서 만나는지 확인
        if (a+1)//2==(b+1)//2: 
            break
        
        # 만나지 않는다면 라운드 증가하고 a,b 인덱스 재설정
        answer+=1
        a=(a+1)//2
        b=(b+1)//2

    return answer

print(solution(8,4,7))


#21년 1월 27일 풀이
#a,b는 만나기 전까지 무조건 이긴다는 가정을 한다.
#a와 b에 -1을 해준 후 같을 때까지 //2를 하면 된다.
#예를 들어 a=1, b=8이면 a=0, b=7을 가지고 //2를 해준다.
#(a,b)=(0,7)->(0,3)->(0,1)->(0,0)이 된다. 즉 3번째 라운드에서 만난다는 것이다.
def solution(n,a,b):
    answer = 3
    cnt=1
    a-=1
    b-=1
    while a!=b:
        a=a//2
        b=b//2
        cnt+=1
    answer=cnt-1
    return answer

print(solution(8,1,6))