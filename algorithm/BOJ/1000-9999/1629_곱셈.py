a,b,c=map(int,input().split())

result=1
def division(a,b):
    if b>1:
        if b%2==0:
            return division(a,b//2)**2%c
        else:
            return division(a,b-1)*a
    else:
        if b==1:
            return a
        else:
            return 1
print(division(a,b)%c)

        