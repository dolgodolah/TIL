# 아스키코드값을 활용하여 chr(97+i)가 입력받은 word안에 있는지 확인하여
# 존재한다면 index값을 추출한다.
word=input()
index = [-1]*26
for i in range(26):
    if chr(97+i) in word:
        index[i]=word.index(chr(97+i))
print(*index)
