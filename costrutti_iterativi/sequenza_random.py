import random

# task 1: genera 10 numeri pseudo-casuali compresi nell'intervallo [1, 10]
print('> task 1')
for _ in range(10):
    numero = random.randint(1, 10)
    print(numero, end='  ')
print()

# task 2: individua il maggiore (max) tra 10 valori random
print('> task 2 (versione con lista)')
lista = []
for _ in range(10):
    numero = random.randint(1, 10)
    print(numero, end='  ')
    # aggiungi alla lista il numero generato casualmente
    lista.append(numero)
print('\nIl valore massimo è', max(lista))

print('> task 2')
max = 0
for _ in range(10):
    numero = random.randint(1, 10)
    print(numero, end='  ')
    if numero > max:
        max = numero
print('\nIl valore massimo è', max)

# task 3: genera casualmente 20 numeri interi compresi nell'intervallo [1, 100] e mostra solo i valori pari
print('> task 3')
for _ in range(20):
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        print(numero, end='  ')
print()

# task 4: genera casualmente 20 numeri interi pari compresi nell'intervallo [1, 100]
print('> task 4')
for _ in range(20):
    numero = random.randrange(2, 101, 2)
    print(numero, end='  ')
print()

# task 5: genera casualmente valori nell'intervallo [1, 100], termina quando avrai generato 10 valori pari.
#         Mostra i 10 valori pari e sostituisci i valori dispari con una 'X'.
print('> task 5')
conta = 0
while conta < 10:
    numero = random.randint(1, 100)
    if numero % 2 == 0:
        print(numero, end='  ')
        conta += 1
    else:
        print('X', end='  ')
print()
