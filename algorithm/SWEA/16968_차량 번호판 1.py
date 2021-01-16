
data =  input()
answer = 0
for i in range(len(data)):
    if i==0:
        if data[i]=='c':
            answer = 26
        elif data[i]=='d':
            answer = 10
    else:
        if data[i]=='c':
            if data[i-1]==data[i]:
                answer = answer*25
            else:
                answer = answer*26
        elif data[i]=='d':
            if data[i-1]==data[i]:
                answer = answer*9
            else:
                answer = answer*10
print(answer)
