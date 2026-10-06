# Scrivi un programma che,
'''
dati due numeri interi in ingresso, 
stabilisca quale dei due ha un valore assoluto maggiore. [FUNZIONE]
'''
def find_max_abs(a, b):
    if a < 0:
        a = -a
    if b < 0:
        b = -b
    if a > b:
        return a
    else:
        return b


m = find_max_abs(5, -12)
print(m)   

'''
dati due numeri in ingresso, 
stampi a video quale dei due ha il quadrato maggiore e il relativo quadrato. [PROCEDURA]
'''
def max_square(a, b):
    if a**2 > b**2:
        print(f'{a} -> {a**2}')
    else:
        print(f'{b} -> {b**2}')


print(max_square(5, -7))

'''
dato un numero intero positivo, 
restituisca 1 se il numero è primo, altrimenti 0. [FUNZIONE]
'''
def is_prime(n):
    dividers = 0
    i = 1
    while dividers <= 2:
        if n%i == 0:
            dividers += 1
        i += 1
    # da completare...
    