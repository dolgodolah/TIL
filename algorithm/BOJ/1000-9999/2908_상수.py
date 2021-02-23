A,B=map(str,input().split())
A=''.join(reversed(list(A)))
B=''.join(reversed(list(B)))
if A<B:
    print(B)
else:
    print(A)