# number를 1씩 늘려가면서 number에 6이 3개 연속으로 나오면 ls에 추가해준다.
# 입력에서 주어진 n개만큼 ls가 채워지면 while문을 멈추고 ls의 마지막을 출력한다.

n=int(input())
number=666
ls=[]
while n>0:
    tmp = str(number)
    check = False
    for i in range(len(tmp)):
        if i+3>len(tmp):
            break
        if tmp[i:i+3]=='666':
            check=True
            break
    if check:
        ls.append(tmp)
        n-=1
    number+=1
print(ls[-1])