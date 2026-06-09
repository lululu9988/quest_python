stud_a:list[int]=[n for n in map(int,input().split())]
stud_b:list[int]=[n for n in map(int,input().split())]

max:str=""

if stud_a[0]==stud_b[0]:
    max="A" if stud_a[1]>stud_b[1] else "B"
elif stud_a[0]>stud_b[0]:
    max="A"
else:
    max="B"

print(max)