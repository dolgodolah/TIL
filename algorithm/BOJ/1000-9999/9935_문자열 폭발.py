# 문자열에 대한 문제는 stack을 잘 활용해야 하는 것 같다.
# 인덱싱 에러를 주의해서 stack 자료구조를 이용한다.
# 폭탄문자와 같은 문자가 stack에 쌓이면 그 길이만큼 pop해준다.

text=input()
bomb=input()
stack=[]
for i in text:
    stack.append(i)
    if len(stack)>=len(bomb):
        if ''.join(stack[-len(bomb):])==bomb:
            for _ in range(len(bomb)):
                stack.pop()
        
if stack:
    print(''.join(stack))
else:
    print("FRULA")