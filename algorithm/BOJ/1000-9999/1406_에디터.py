import sys
from collections import deque
input=sys.stdin.readline
text=list(input().strip())
stack=list()
N=int(input())
for _ in range(N):
    command=input().split()
    if command[0]=='L':
        if text:
            stack.append(text.pop())
    elif command[0]=='D':
        if stack:
            text.append(stack.pop())
    elif command[0]=='B':
        if text:
            text.pop()
    else:
        text.append(command[1])
answer=''.join(text)+''.join(stack[::-1])
print(answer)