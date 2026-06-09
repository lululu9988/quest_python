lst_a:list[int]=[n for n in map(int,input().split())]
lst_b:list[int]=[n for n in map(int,input().split())]

print(1 if lst_a[0]>lst_b[0] and lst_a[1]>lst_b[1] else 0)