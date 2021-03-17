# 주어진 점수들을 중간고사(35%)+기말고사(45%)+과제(20%) 비율에 맞춰 환산하고
# k번째 학생의 순위를 알아낸다.
# 해당 순위가 grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0'] 중에 어디에 해당되는지
# grade[rank//(n//10)]를 통해 계산한다.

T=int(input())
for t in range(1,T+1):
    n,k=map(int,input().split())
    students=[0]*(n)
    for i in range(n):
        a,b,c=map(int,input().split())
        students[i]=(i,a*0.35+b*0.45+c*0.2)
    students.sort(key=lambda x:-x[1])
    for i in range(len(students)):
        if students[i][0]==k-1:
            rank=i
            break

    grade=['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']
    print(f"#{t} {grade[rank//(n//10)]}")

