n=int(input())
people = []
for i in range(n):
    people.append(list(map(int,input().split())))
answer=[]
for i in range(n):
    rating = 1
    for j in range(n):
        if people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            rating+=1
    answer.append(rating)
print(*answer)