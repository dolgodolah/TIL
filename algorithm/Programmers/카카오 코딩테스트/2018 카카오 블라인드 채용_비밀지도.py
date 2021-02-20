# 10진수를 2진수로 표현하는 함수 bin
# bin(10) -> 0b1010, bin(10)[2::] -> 1010

# arr1[i]와 arr2[i]의 값을 or연산을 하여 나온 값을 2진수로 치환하면 된다.
# or연산을 통해 나온 값들은 이진수로 변환했을 때의 길이가 n이하라고 조건에서 나왔기때문에
# for _ in range(n):
#   if num%2==0:
#       temp=" "+temp
#   else:
#       temp="#"+temp
#   num//=2
#
# 위와같이 n번 수행해주면 된다.

# 새로운 풀이
def solution(n,arr1,arr2):
    answer=[]
    for i in range(n):
        a=arr1[i]
        b=arr2[i]
        num=a|b
        temp=''
        for _ in range(n):
            if num%2==0:
                temp=" "+temp
            else:
                temp="#"+temp
            num//=2
        answer.append(temp)
    return answer



# 새싹 시절 풀이
def solution(n, arr1, arr2):
    answer = []
    map1,map2=[],[] #10진수로 주어진 arr1,arr2를 2진수로 바꿔 저장할 공간이다.

    for i in arr1: #지도1의 2진수 변환!
        temp=bin(i)[2:] #지도로 표현하기 위해서는 2진수의 길이가 n만큼 되어야한다.
        if len(temp)<n: #예를 들어 5x5 지도일 경우 2진수의 길이는 5가 되어야하는데
            for _ in range(n-len(temp)): #3(10)을 2진수로 변환 시 11이 된다.
                temp='0'+temp #그러면 11을 길이가 5가 되게끔 0을 붙여준다. 11->00011
        map1.append(temp) #최종 변환된 2진수를 지도에 넣는다.
    
    for i in arr2:#지도2의 2진수 변환!
        temp=bin(i)[2:]
        if len(temp)<n:
            for _ in range(n-len(temp)):
                temp='0'+temp
        map2.append(temp)

    new_map=[[' ']*n for _ in range(n)] #map1과 map2를 겹쳐 암호를 해독한 지도
    for i in range(n):
        for j in range(n):
            if map1[i][j]=='1' or map2[i][j]=='1': #map1과 map2의 해당 칸이 둘 중에 하나라도 벽이면
                new_map[i][j]='#' #새로운 지도에서도 벽이다.
    
    #완성된 비밀지도를 출력형식에 맞춘다.
    for i in range(n):
        temp=''
        for j in range(n):
            temp+=new_map[i][j]
        answer.append(temp)

    return answer
            

print(solution(5,[9, 20, 28, 18, 11],[30, 1, 21, 17, 28]))