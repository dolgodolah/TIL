# 파이썬 dict 구조를 이용해 쉽게 해결할 수 있었다.
# 소수점 넷째자리까지 반올림하여 출력해야 하는데 round의 경우 1.0000를 1.0으로 출력해준다.
# 온전히 1.0000으로 출력하기 위해서는 %.4f를 이용하여야 한다. print('%.4f' %1.0000)

import sys
input=sys.stdin.readline

trees=dict()
cnt=0
while True:
    tree=input().strip()
    if not tree:
        break

    if tree in trees:
        trees[tree]+=1
    else:
        trees[tree]=1
    cnt+=1
names=sorted(trees)
for name in names:
    # print(name+" "+str(round(trees[name]/cnt*100,4)))
    print('%s %.4f' %(name, trees[name]/cnt*100))
