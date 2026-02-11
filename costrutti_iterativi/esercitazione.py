'''
Scrivere un programma che:
- chieda all’utente un numero intero n;
- stampi su una sola riga tutti i multipli di n compresi tra 0 e 100 (estremi esclusi);
- stampi quanti multipli sono stati trovati.

Esempio di output con n = 7:
7  14  21  28  35  42  49  56  63  70  77  84  91  98
Totale: 14
'''
n = int(input('Inserire un valore intero: '))
conta = 0
for multiplo in range(n, 100, n):
    print(multiplo, end='  ')
    conta += 1
print('\nTotale:', conta)

'''
Scrivere un programma che:
- generi numeri casuali tra 1 e 50 (estremi inclusi);
- continui la generazione finché non vengono trovati k numeri multipli di n;
- stampi i numeri multipli di n;
- sostituisca tutti gli altri numeri con il carattere X.

Esempio di output con n = 7 e k = 5:
X 14 X 35 X X 7 X 28 X X 49
'''
import random

n, k = 2, 5
while k > 0:
    numero = random.randint(1, 50)
    if numero % n == 0:
        print(numero, end=' ')
        k -= 1
    else:
        print('X', end=' ')
print()

'''
Scrivere un programma che, dato un numero intero n (n ≥ 2), stampi un triangolo rettangolo 
vuoto avente base n-1 simboli "_" e altezza n simboli "|".

Esempio di output con n = 4:
|\
| \
|  \
|___\
'''
n = int(input('Inserire valore '))
while n < 2:
    n = int(input('Valore errato.\n n >= 2 -> '))

# completa esercizio...