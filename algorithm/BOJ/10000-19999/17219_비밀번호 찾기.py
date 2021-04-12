import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dic=dict()
for _ in range(n):
    url,password=input().split()
    dic[url]=password

for _ in range(m):
    print(dic[input().strip()])