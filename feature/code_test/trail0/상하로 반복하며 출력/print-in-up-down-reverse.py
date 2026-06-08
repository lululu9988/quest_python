num=int(input())
lst:list[int]=[n for n in range(1,num+1)]

for i in range(num):
    for j in range(num):
        if j%2==0:
            print(lst[i],end="")
        else:
            print(lst[num-1-i],end="")
    print()