'''
# task 0: stampa numeri nell'intervallo [0, n-1], con n letto in input
n = int(input('Inserire valore n: '))
for i in range(n):
    print(i)

# task 1: stampa numeri nell'intervallo [n, 1], su una sola riga
for i in range(n, 0, -1):
    print(i, end=' ')
print()

# task 2: stampa i valori pari nell'intervallo [n, n^2] -> n^2 è il quadrato di n
for i in range(n, n**2 + 1):
    if i%2 == 0:
        print(i)
'''
# task 3: stampa i multipli di x (letto in input) minori di 100
x = int(input('Inserire valore x: '))
# for i in range(x, 100, x):
#     print(i)

# task 4: stampo, su righe diverse, le tabelline dei valori nell'intervallo [1, x]
for t in range(1, x+1):     
    for i in range(t, t*10 + 1, t):
        print(i, end=' ')
    print()
