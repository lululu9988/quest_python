count=int(input())
lst_sum:list[int]=[]
a=0
b=0
sum=0

for _ in range(count):
    a,b=input().split()
    a=int(a)
    b=int(b)
    for j in range(a,b+1):
        if j%2==0:
            sum+=j
    lst_sum.append(sum)
    sum=0

for k in lst_sum:
    print(k)
