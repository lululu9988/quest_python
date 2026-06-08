#입력받은 두 개의 2차원 격자 비교하기.
n,m=map(int,input().split())
lst:list[list[list]]=[]

for _ in range(2):
    lst.append([list(map(int,input().split())) for _ in range(n)])

for i in range(n):
    for j in range(m):
        if lst[0][i][j] == lst[1][i][j]:
            print("0", end=" ")
        else:
            print("1", end=" ")
    print()