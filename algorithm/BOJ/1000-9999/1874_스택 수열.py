import sys
input=sys.stdin.readline
n=int(input())
ls=list()
stack=list()
answer=list()
idx=1
for _ in range(n):
    num=int(input())
    while idx<=num:
        stack.append(idx)
        answer.append('+')
        idx+=1
    if stack[-1]==num:
        stack.pop()
        answer.append('-')
if stack:
    print("NO")
else:
    for i in answer:
        print(i)