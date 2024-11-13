a = [1, 4, 6]
b = [2, 5, 7]
c = list()

i, j = 0, 0
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

if i < len(a):
    for e in a[i:]:
        c.append(e)

if j < len(b):
    for e in b[j:]:
        c.append(e)

print(c)