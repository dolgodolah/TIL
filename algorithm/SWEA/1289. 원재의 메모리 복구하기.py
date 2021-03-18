# 현재 메모리값과 타켓 메모리값을 앞에서부터 인덱스마다 비교하여 다를 경우
# 해당 인덱스부터 끝까지 타켓메모리[i]로 바꿔준다.

# 위 과정의 반복횟수가 정답이다.

T=int(input())
for t in range(1,T+1):
    target=list(input())
    num=['0']*len(target)
    answer=0
    for i in range(len(target)):
        if target[i]!=num[i]:
            answer+=1
            if target[i]=='0':
                for j in range(i,len(target)):
                    num[j]='0'
            else:
                for j in range(i,len(target)):
                    num[j]='1'
    print(f"#{t} {answer}")
