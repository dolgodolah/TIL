# 해시(dict)를 이용했다. enroll[i] - referral[i] 의 key-value형태로 tree 하나를 만들고,
# enroll에 있는 이름마다 수익금을 갱신할 profits도 만들어준다. -> {'-' : 0, 'john' : 0, 'mary' : 0, ..., 'young' : 0}

# 판매금액의 10%를 뺀 금액을 해당 판매원의 profits[seller[i]]에 더해주고
# 나머지 10% 금액에 대해서는 tree를 타 추천인에 대해서 다시 이 과정을 반복한다.

def solution(enroll, referral, seller, amount):
    answer = []
    tree=dict()
    profits={'-':0}
    for i in range(len(enroll)):
        tree[enroll[i]]=referral[i]
        profits[enroll[i]]=0
    for i in range(len(seller)):
        profit=amount[i]*100
        remainder=int(profit/10)
        profits[seller[i]]+=profit-remainder
        name=tree[seller[i]]
        while name in tree:
            profit=remainder
            remainder=int(profit/10)
            profits[name]+=profit-remainder
            name=tree[name]
    for name in enroll:
        answer.append(profits[name])
    return answer


print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],["young", "john", "tod", "emily", "mary"],[12, 4, 2, 5, 10]))
