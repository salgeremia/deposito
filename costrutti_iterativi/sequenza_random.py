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
