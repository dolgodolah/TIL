import sys
from collections import deque
n=int(input())
for _ in range(n):
    ls=list(input())
    stack=[ls[0]]
    for i in range(1,len(ls)):
        if stack and stack[-1]=='(':
            if ls[i]==')':
                stack.pop()
            else:
                stack.append(ls[i])
        else:
            stack.append(ls[i])
    if stack:
        print("NO")
    else:
        print("YES")