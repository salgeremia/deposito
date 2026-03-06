# 05/03/2026

# Lezione 1 - Costrutto iterativo indefinito WHILE

# Esempio 1: conto alla rovescia.
x = 10
while x > 0:
    print(x)
    x -= 1
# Abbiamo fatto bene ad utilizzare il costrutto WHILE?
# RISPOSTA: sarebbe stato meglio utilizzare il costrutto FOR.
for x in range(10, 0, -1):
    print(x)
# Ora va decisamente meglio!

# Esempio 2: sottrazioni random con risultato positivo.
import random

n = int(input('Inserire valore intero positivo: '))
x = n
while x > 0:
    print(x)
    y = random.randint(1, n)
    x -= y

# Esempio 3: gestione dati di input.
'''TRACCIA: la temperatura di una serra deve essere compresa tra [15, 39] gradi.
Chiedere all'utente di inserire la temperatura attualmente registrata.
Se la temperatura non è valida, chiedere all'utente di inserire nuovamente il valore,
altrimenti terminare il programma.
'''
valore = int(input('Inserire temperatura della serra: '))
while valore < 15 or valore > 39:
    valore = int(input('Inserire temperatura della serra: '))
print('Temperatura corretta!')

# Lezione 2 - Costrutto iterativo indefinito FOR

# Esempio 1: stampare i singoli elementi da una lista.
colori = ['rosso', 'blu', 'viola', 'giallo', 'verde']
for x in colori:
    print(x)

# Esempio 2: stampa la tabellina del numero n letto in input.
'''
input:  n = 6
output: 6 x 1 = 6
        6 x 2 = 12
        6 x 3 = 18
        ...
        6 x 10 = 60
'''
n = int(input('Inserire un valore: '))
for i in range(1, 11):
    print(n, 'x', i, '=', n*i)
    # in alternativa...
    # print(f'{n} x {i} = {n*i}')

# Esempio 3: stampa una riga composta dal simbolo * ripetuto n volte.
n = 5
for _ in range(n):
    print('*', end=' ')
print()
# in alterantiva...
# print('* ' * n)

# Esempio 4: stampa il simbolo * su m righe e n colonne.
m, n = 4, 3
for i in range(m):
    for j in range(n):
        print('*', end=' ')
    print()
# in alternativa...
'''
m, n = 4, 3
for _ in range(m):
    print('* ' * n)
'''

# Esempio 5: stampa valori da 1 a m su n righe.
'''
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
'''
n, m = 4, 5
for _ in range(n):
    for i in range(1, m+1):
        print(i, end=' ')
    print()

# Esempio 6: stampa valori da 1 a m, disposti in forma triangolare, su n righe.
'''
1 
1 2 
1 2 3 
1 2 3 4 
1 2 3 4 5
'''
n = 5

for j in range(1, n+1): 
    for i in range(1, j+1):
        print(i, end=' ')
    print()
