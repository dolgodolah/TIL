import sys
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))
b, c = map(int,input().split())

answer = 0
for i in A:
    num = i - b
    if num<=0:
        answer+=1
        continue
    answer += 1 + (num//c)
    if num%c > 0 :
        answer+=1
print(answer)