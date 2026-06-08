num=int(input())
lst:list[int]=[n for n in range(1,num+1)]

for i in range(num):
    if i%2!=1:
        for j in range(num):
            print(lst[j],end="")
    else:
        for j in range(num):
            print(lst[(num-1)-j],end="")
    print()
