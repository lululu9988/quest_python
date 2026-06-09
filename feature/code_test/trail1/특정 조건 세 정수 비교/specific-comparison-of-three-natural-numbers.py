lst:list[int]=[n for n in map(int,input().split())]
min=min(lst)

print(1 if lst[0]==min else 0,end=" ")
print(1 if lst[0]== lst[1]==lst[2] else 0)
