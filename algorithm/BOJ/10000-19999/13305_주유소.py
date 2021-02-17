n=int(input())
distance=list(map(int,input().split()))
cost=list(map(int,input().split()))

answer=0
min_cost=cost[0]
sum_distance=0
for i in range(n-1):
    if cost[i]<min_cost:
        answer+=sum_distance*min_cost
        min_cost=cost[i]
        sum_distance=distance[i]
    else:
        sum_distance+=distance[i]

answer+=sum_distance*min_cost
print(answer)