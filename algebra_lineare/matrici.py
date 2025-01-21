m = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 2, 2 ,2],
     [3, 3, 3, 3]]

dim = 4

for row in range(dim):
    for col in range(dim):
        print(m[row][col], end=' ')
    print()
print()

for row in m:
    for i in row:
        print(i, end=' ')
    print()
print()

for row in m:
    print(*row)