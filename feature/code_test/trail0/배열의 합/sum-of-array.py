lst:list[list]=[list(map(int,input().split())) for _ in range(4)]

for n in range(4):
    print(sum(lst[n]))
