# ou have two strings of lowercase English letters. You can perform two types of operations on the first string:

# 1. Append a lowercase English letter to the end of the string.
# 2. Delete the last character of the string. Performing this operation on an empty string results in an empty string.
# Given an integer, k, and two strings, s and t, determine whether or not you can convert s to t by performing exactly k of the above operations on s. If it's possible, print Yes. Otherwise, print No.


s = list(input())
t = list(input())
k = int(input())
a = len(s)
b = len(t)
for i in range(min(len(s),len(t))):
    if s[i]==t[i]:
        a-=1
        b-=1
    else:
        break

cnt=a+b #s에서 t로 바꾸려면 Append and Delete 해야할 정확한 횟수를 cnt라 할거다.
if cnt==k or len(s)+len(t)<=k: #cnt와 k가 일치하는 경우 또는 s를 다 지우고 t를 다 추가해도 k가 남으면 무조건 yes다
    print('Yes')
elif cnt%2==k%2 and cnt<=k: #cnt가 k보다 크면 일단 답없다. k보다 작거나 같다면 추가,삭제 연산의 짝이 맞아야한다.
    #예를 들어 (a,b,c,d,e),(a,b,d),k=6이면 cnt=4이기때문에 추가,삭제 연산의 짝이 맞다.
    print('Yes')
else:
    print('No')