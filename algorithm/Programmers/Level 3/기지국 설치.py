# N의 최대크기가 200,000,000이기때문에 N을 완전탐색하면 시간초과가 발생할 것 같았다.
# 최대 크기가 10,000인 stations을 탐색했다.
# stations[i]를 기준으로 왼쪽부분에 전파가 모두 전달되게 하기 위해서 몇 개의 기지국이 필요한지 연산한다.
# 모든 stations에 대해 위 연산을 하고 나면 마지막 stations 기준으로 오른쪽 부분에 대한 처리를 해야한다.

def solution(n, stations, w):
    answer = 0
    last = 0
    
    for i in range(len(stations)):
        #stations[i] 기준 왼쪽
        tmp=stations[i]-1-w-last
        if tmp%((w*2)+1)==0:
            answer+=tmp//((w*2)+1)
        else:
            answer+=tmp//((w*2)+1)+1
        last=stations[i]+w

    #last가 n보다 크면 모든 아파트에 전파가 전달되는 것이기 때문에 마지막 기지국 기준 오른쪽에 대한 처리를 하지 않아도 된다.
    if last<n:
        if (n-last)%((w*2)+1)==0:
            answer+=(n-last)//((w*2)+1)
        else:
            answer+=(n-last)//((w*2)+1)+1
    
    return answer

print(solution(11,[4,11],1))
print(solution(16,[9],2))