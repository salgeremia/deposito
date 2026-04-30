valore = 9
for row in range(valore):
    n = 0
    for col in range(valore):
        if col <= row:
            n += 1
        print(n, end=' ')
    print()