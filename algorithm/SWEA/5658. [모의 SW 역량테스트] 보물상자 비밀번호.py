#10진수 -> 16진수 hex(15), 16진수 -> 10진수 int('ffff',16)
from collections import deque
T = int(input())
for t in range(1,T+1):
    n,k=map(int,input().split())
    s=list(input())
    dic = dict()
    for _ in range(len(s)//4):
        for i in range(0,len(s),len(s)//4):
            if not ''.join(s[i:i+len(s)//4]) in dic:
                dic[''.join(s[i:i+len(s)//4])]=1
        s.insert(0,s.pop())
    # print(dic)
    ls=list(dic.keys()) #회전별로 나온 모든 16진수들을 담는다.
    ls.sort(reverse=True)
    print(f"#{t} {int(ls[k-1].lower(),16)}")


