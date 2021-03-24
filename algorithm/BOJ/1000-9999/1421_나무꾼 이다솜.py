import sys
input=sys.stdin.readline
n,c,w=map(int,input().split())
trees=list()
for _ in range(n):
    trees.append(int(input()))

max_v=max(trees)
answer=0
for length in range(1,max_v+1):
    tmp=0
    for tree in trees:
        if tree%length==0:
            if tree==length:
                if tree*w>0:
                    tmp+=tree*w
            else:
                if (tree*w)-(tree//length-1)*c>0:
                    tmp+=(tree*w)-(tree//length-1)*c
        else:
            if (length*(tree//length))*w-(tree//length*c)>0:
                tmp+=(length*(tree//length))*w-(tree//length*c)
    answer=max(answer,tmp)
print(answer)