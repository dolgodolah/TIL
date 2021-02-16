# 그리디 문제이다. 최솟값이 나오려면 시간이 적게 걸리는 사람부터 atm를 이용해야한다.

n=int(input())
people=list(map(int,input().split()))
people.sort()
answer=people[0]
wait=people[0]
# 1 2 3 4 5
for i in range(1,len(people)):
    answer+=wait+people[i]
    wait+=people[i]
print(answer)