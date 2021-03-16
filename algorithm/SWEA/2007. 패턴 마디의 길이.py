# 비교문자를 1부터 늘려가며 마디(패턴에서 반복되는 부분)인지 확인한다.
# 최초 마디를 발견 시 탐색을 중지하고 갱신한 answer을 출력한다.

T=int(input())
for t in range(1,T+1):
    text=input()
    answer=0
    for i in range(1,len(text)+1):
        tmp=text[:i]
        for j in range(i,len(text),i):
            if tmp==text[j:j+i]:
                answer=i
                break
            else:
                break
        if answer!=0:
            break
    print(f"#{t} {answer}")