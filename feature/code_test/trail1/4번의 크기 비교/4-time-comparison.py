a=int(input())
lst:list[int]=[n for n in map(int,input().split())]

for i in range(4):
    print(1 if a>lst[i] else 0)