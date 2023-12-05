# Bubble Sort

l = [5, 2, 8, 9, 3, 1]
# l.sort()
print(l)
print('- - - -')

for j in range(len(l)-1):
    scambi = False
    for i in range(len(l)-1-j):
        if l[i] > l[i+1]:               # confronta
            l[i], l[i+1] = l[i+1], l[i] # scambia
            scambi = True
        print(l)
    print()
    if scambi == False:
        break