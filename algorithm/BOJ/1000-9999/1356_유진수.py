#처음 숫자를 받을 때 int형이 아닌 str형으로 받아 인덱싱을 통해 연산을 수행한다.

num=input()

for i in range(1,len(num)):
    left=num[:i]
    right=num[i:]
    left_value=1
    right_value=1
    for j in left:
        left_value*=int(j)
    for j in right:
        right_value*=int(j)
    if left_value==right_value:
        print("YES")
        break
else:
    print("NO")