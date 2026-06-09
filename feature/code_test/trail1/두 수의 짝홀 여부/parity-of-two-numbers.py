lst:list[int]=[n for n in map(int,input().split())]

for i in range(2):
    if lst[i]%2==0:
        print("even")
    else:
        print("odd")
