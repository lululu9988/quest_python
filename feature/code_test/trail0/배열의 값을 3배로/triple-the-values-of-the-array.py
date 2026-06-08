
lst = [[n * 3 for n in map(int, input().split())] for _ in range(3)]

for i in range(3):
    for j in range(3):
        print(lst[i][j], end=" ")
    print()