# Dato un valore k
k = 7

print('\n> TASK 1: ', end='')
# stampare tutti i valori interi positivi nell'intervallo [1, k)
i = 1
while i < k:
    print(i, end=' ')
    i += 1

print('\n> TASK 2: ', end='')
# stampare tutti i valori interi positivi nell'intervallo [1, 10] eccetto k
i = 1
while i <= 10:
    if i != k:
        print(i, end=' ')
    i += 1

print('\n> TASK 3: ', end='')
# stampare tutti i valori interi positivi nell'intervallo [1, 10] 
# sostituendo il valore k con una 'X'
i = 1
while i <= 10:
    if i != k:
        print(i, end=' ')
    else:
        print('X', end=' ')
    i += 1

print('\n> TASK 4: ', end='')
# stampare le somme incrementali dei valori interi positivi 
# nell'intervallo [1, 10] escludendo il valore k
i, somma = 0, 0
while i < 10:
    i += 1
    if i == k:
        continue
    somma += i
    print(somma, end=' ')

print('\n> TASK 5: ', end='?\n')
# stampare le 10 somme incrementali dei valori interi positivi 
# nell'intervallo [1, 10]. 
# Se le somme incremenali sono maggiori di k^2, stampa -1.
'''
Esempio: 
 ____________________________________
| input | output                     |
|-------|----------------------------|
| k = 4 | -1                         |
| k = 8 | 1 3 6 10 15 21 28 36 45 55 |  
 ------------------------------------
'''