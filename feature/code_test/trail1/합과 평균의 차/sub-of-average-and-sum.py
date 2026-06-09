lst:list[int]=[n for n in map(int,input().split())]
sum=sum(lst)
print(sum,int(sum/3),int(sum*(2/3)),sep="\n")