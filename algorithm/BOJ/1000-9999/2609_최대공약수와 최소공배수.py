a,b=map(int,input().split())
num=a*b
if b>a:
    a,b=b,a

while b>0:
    tmp=a%b
    a=b
    b=tmp
print(a)
print(num//a)
