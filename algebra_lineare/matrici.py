m = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 2, 2 ,2],
     [3, 3, 3, 3]]

for i in range(4):
    for j in range(4):
        print(m[i][j], end=' ')
    print()
print()


for row in m:
    for i in row:
        print(i, end=' ')
    print()
print()

for row in m:
    print(*row)