#보자마자 숫자가 너무 많아서 덜컥 겁이 났는데 천천히 읽어보면서 이해만 하면 된다.
#문자열을 적절히 잘라서 다중집합을 만들고, 교집합과 합집합을 유도하면 된다.

import math
def solution(str1, str2):
    answer = 0
    str1=str1.lower()
    str2=str2.lower()
    A,B=[],[]
    for i in range(len(str1)-1):
        if 97<=ord(str1[i])<=122 and 97<=ord(str1[i+1])<=122:
            A.append(str1[i]+str1[i+1])

    for i in range(len(str2)-1):
        if 97<=ord(str2[i])<=122 and 97<=ord(str2[i+1])<=122:
            B.append(str2[i]+str2[i+1])
    # print(A,B)
    n,nn=0,0
    for i in A:
        for j in range(len(B)):
            if i==B[j]:
                n+=1
                B.pop(j)
                break
        nn+=1
    nn+=len(B)
    if nn==0:
        answer=65536
    else:
        answer=math.floor(n/nn*65536)
    return answer

# print(solution('FRANCE','french'))
# print(solution('handshake','shake hands'))
print(solution('E=M*C^2	','e=m*c^2'))
