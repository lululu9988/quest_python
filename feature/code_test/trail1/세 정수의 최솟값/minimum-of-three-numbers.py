a,b,c=map(int,input().split())
min_lst:list[int]=[]

min_lst.append(a if a<b else b)
min_lst.append(b if b<c else c)
print(min_lst[0] if min_lst[0]<min_lst[1] else min_lst[1])