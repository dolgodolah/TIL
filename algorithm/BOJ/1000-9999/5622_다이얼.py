word=input()

dial=[('ABC',2),('DEF',3),('GHI',4),('JKL',5),('MNO',6),('PQRS',7),('TUV',8),('WXYZ',9)]

answer=0
for a in word:
    for b in dial:
        if a in b[0]:
            answer+=b[1]+1
            break
print(answer)