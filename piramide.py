def piramide(n):
    sfere = 0
    for i in range(n, 0, -1):
        sfere += i*(i+1)/2
    return int(sfere)

print(piramide(4))