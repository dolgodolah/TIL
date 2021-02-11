# n=123일 때 분해합은 123+1+2+3, 129이다.
# 즉 123은 129이 생성자인것이다.
# 문제에서 주어진 n은 분해합이 주어진 것이고, 구해야하는 답은 생성자를 출력해야한다.

# n=216이 주어졌을 때
# 1부터 215까지 완전탐색을 한다. sum(list(map(int,str(i))))+i를 통해 분해합을 구현했다.
# 분해합이 n과 일치하지 않고 정답을 출력하지 못한다면 for else문을 통해 0을 출력한다.


n=int(input())

for i in range(1,n):
    if sum(list(map(int,str(i))))+i==n:
        print(i)
        break
else:
    print(0)