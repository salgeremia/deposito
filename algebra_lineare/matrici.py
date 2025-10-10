m = [[0, 0, 0, 0],
     [1, 1, 1, 1],
     [2, 2, 2 ,2],
     [3, 3, 3, 3]]

dim = 4
k = 5

c = [[1 for j in range(dim)] for i in range(dim)]
print(c)
for row in range(dim):
    for col in range(dim):
        c[row][col] = m[row][col] * k

print(c)

'''
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
'''