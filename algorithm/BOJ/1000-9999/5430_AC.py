import sys
from collections import deque
# input=sys.stdin.readline
t=int(input())
for _ in range(t):
    commands=list(input())
    n=int(input())
    array=input()
    array=array.lstrip('[')
    # array=array.rstrip('\n')
    array=array.rstrip(']')
    if array:
        array=list(map(int,array.split(',')))
    array=deque(array)
    reversed_check=False
    for command in commands:
        if command=='R':
            if reversed_check==False:
                reversed_check=True
            else:
                reversed_check=False
        elif command=='D':
            if reversed_check==False:
                if array:
                    array.popleft()
                else:
                    print("error")
                    break
            else:
                if array:
                    array.pop()
                else:
                    print("error")
                    break
    else:
        if reversed_check==True:
            print("[",end="")
            if array:
                if len(array)>1:
                    print(array[-1],end=",")
                    for i in range(len(array)-2,0,-1):
                        print(array[i],end=",")
                print(array[0],end="")
            print("]")
        else:
            print("[",end="")
            if array:
                if len(array)>1:
                    print(array[0],end=",")
                    for i in range(1,len(array)-1):
                        print(array[i],end=",")
                print(array[len(array)-1],end="")
            print("]")