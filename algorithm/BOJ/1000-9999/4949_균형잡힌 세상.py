while True:
    text=input()
    if text=='.':
        break
    stack=[]
    for i in text:
        if i=='(':
            stack.append(i)
        elif i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                stack.append(i)
        elif i=='[':
            stack.append(i)
        elif i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                stack.append(i)
    if not stack:
        print("yes")
    else:
        print("no")